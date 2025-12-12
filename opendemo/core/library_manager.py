"""
库管理器模块

负责管理库的元数据、功能列表和 demo 组织。
"""

import json
from pathlib import Path
from typing import Dict, Any, Optional, List, Tuple
from opendemo.core.demo_manager import Demo
from opendemo.utils.logger import get_logger

logger = get_logger(__name__)


class LibraryManager:
    """库管理器类"""
    
    def __init__(self, storage_service, demo_manager):
        """
        初始化库管理器
        
        Args:
            storage_service: 存储服务实例
            demo_manager: Demo管理器实例
        """
        self.storage = storage_service
        self.demo_manager = demo_manager
    
    def get_library_info(
        self,
        language: str,
        library: str
    ) -> Optional[Dict[str, Any]]:
        """
        获取库的完整信息
        
        Args:
            language: 编程语言
            library: 库名称
            
        Returns:
            库信息字典，包含元数据和功能列表
        """
        # 加载库元数据
        metadata = self._load_library_metadata(language, library)
        if not metadata:
            return None
        
        # 获取功能列表
        features = self.list_library_features(language, library)
        
        return {
            'metadata': metadata,
            'features': features,
            'feature_count': len(features)
        }
    
    def list_library_features(
        self,
        language: str,
        library: str,
        category: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        列出库的功能模块
        
        Args:
            language: 编程语言
            library: 库名称
            category: 可选的分类过滤
            
        Returns:
            功能模块列表
        """
        features = []
        
        # 从内置库扫描
        builtin_library_dir = (
            self.storage.builtin_library_path / 
            language.lower() / 
            'libraries' / 
            library
        )
        if builtin_library_dir.exists():
            features.extend(self._scan_library_features(builtin_library_dir))
        
        # 从用户库扫描
        user_library_dir = (
            self.storage.user_library_path / 
            language.lower() / 
            'libraries' / 
            library
        )
        if user_library_dir.exists():
            features.extend(self._scan_library_features(user_library_dir))
        
        # 从输出目录扫描
        output_library_dir = (
            self.storage.get_output_directory() / 
            language.lower() / 
            'libraries' / 
            library
        )
        if output_library_dir.exists():
            output_features = self._scan_library_features(output_library_dir)
            # 去重：输出目录的 demo 可能已存在于内置/用户库
            existing_names = {f['name'] for f in features}
            for feat in output_features:
                if feat['name'] not in existing_names:
                    features.append(feat)
        
        # 按分类过滤
        if category:
            features = [f for f in features if f.get('category') == category]
        
        return features
    
    def search_library_feature(
        self,
        language: str,
        library: str,
        keyword: str
    ) -> List[Tuple[Dict[str, Any], float]]:
        """
        搜索库中的功能
        
        Args:
            language: 编程语言
            library: 库名称
            keyword: 搜索关键字
            
        Returns:
            匹配的功能列表，每项包含 (feature_dict, score)
        """
        all_features = self.list_library_features(language, library)
        
        if not all_features:
            return []
        
        keyword_lower = keyword.lower()
        scored_features = []
        
        for feature in all_features:
            score = self._calculate_feature_match_score(feature, keyword_lower)
            if score > 0:
                scored_features.append((feature, score))
        
        # 按分数降序、难度升序、名称升序排序
        scored_features.sort(
            key=lambda x: (
                -x[1],  # 分数降序
                self._difficulty_rank(x[0].get('difficulty', 'beginner')),  # 难度升序
                x[0]['name']  # 名称升序
            )
        )
        
        return scored_features
    
    def get_feature_demo(
        self,
        language: str,
        library: str,
        feature: str
    ) -> Optional[Demo]:
        """
        获取具体功能的 demo
        
        Args:
            language: 编程语言
            library: 库名称
            feature: 功能模块名称
            
        Returns:
            Demo 对象，未找到返回 None
        """
        # 优先从输出目录查找
        output_demo_path = (
            self.storage.get_output_directory() / 
            language.lower() / 
            'libraries' / 
            library / 
            feature
        )
        if output_demo_path.exists():
            demo = self.demo_manager.load_demo(output_demo_path)
            if demo:
                return demo
        
        # 从用户库查找
        user_demo_path = (
            self.storage.user_library_path / 
            language.lower() / 
            'libraries' / 
            library / 
            feature
        )
        if user_demo_path.exists():
            demo = self.demo_manager.load_demo(user_demo_path)
            if demo:
                return demo
        
        # 从内置库查找
        builtin_demo_path = (
            self.storage.builtin_library_path / 
            language.lower() / 
            'libraries' / 
            library / 
            feature
        )
        if builtin_demo_path.exists():
            demo = self.demo_manager.load_demo(builtin_demo_path)
            if demo:
                return demo
        
        return None
    
    def copy_feature_to_output(
        self,
        language: str,
        library: str,
        feature: str
    ) -> Optional[Path]:
        """
        将库功能 demo 复制到输出目录
        
        Args:
            language: 编程语言
            library: 库名称
            feature: 功能模块名称
            
        Returns:
            输出路径，失败返回 None
        """
        demo = self.get_feature_demo(language, library, feature)
        if not demo:
            return None
        
        output_dir = self.storage.get_output_directory()
        target_path = output_dir / language.lower() / 'libraries' / library / feature
        
        if self.storage.copy_demo(demo.path, target_path):
            return target_path
        
        return None
    
    def _scan_library_features(self, library_dir: Path) -> List[Dict[str, Any]]:
        """
        扫描库目录下的功能模块
        
        Args:
            library_dir: 库目录路径
            
        Returns:
            功能模块列表
        """
        features = []
        
        for item in library_dir.iterdir():
            # 跳过非目录和特殊文件
            if not item.is_dir() or item.name.startswith('_') or item.name.startswith('.'):
                continue
            
            # 尝试读取 metadata.json
            metadata_file = item / 'metadata.json'
            if metadata_file.exists():
                try:
                    with open(metadata_file, 'r', encoding='utf-8') as f:
                        metadata = json.load(f)
                    
                    features.append({
                        'name': item.name,
                        'path': str(item),
                        'title': metadata.get('title', item.name),
                        'description': metadata.get('description', ''),
                        'difficulty': metadata.get('difficulty', 'beginner'),
                        'keywords': metadata.get('keywords', []),
                        'category': metadata.get('category', '未分类'),
                        'library': metadata.get('library', ''),
                        'metadata': metadata
                    })
                except Exception as e:
                    logger.error(f"Failed to load feature metadata from {metadata_file}: {e}")
        
        return features
    
    def _load_library_metadata(
        self,
        language: str,
        library: str
    ) -> Optional[Dict[str, Any]]:
        """
        加载库元数据
        
        Args:
            language: 编程语言
            library: 库名称
            
        Returns:
            元数据字典，失败返回 None
        """
        # 优先从用户库加载
        user_metadata_path = (
            self.storage.user_library_path / 
            language.lower() / 
            'libraries' / 
            library / 
            '_library.json'
        )
        
        if user_metadata_path.exists():
            try:
                with open(user_metadata_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Failed to load user library metadata: {e}")
        
        # 从内置库加载
        builtin_metadata_path = (
            self.storage.builtin_library_path / 
            language.lower() / 
            'libraries' / 
            library / 
            '_library.json'
        )
        
        if builtin_metadata_path.exists():
            try:
                with open(builtin_metadata_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                logger.error(f"Failed to load builtin library metadata: {e}")
        
        return None
    
    def _calculate_feature_match_score(
        self,
        feature: Dict[str, Any],
        keyword: str
    ) -> float:
        """
        计算功能模块的匹配分数
        
        Args:
            feature: 功能模块字典
            keyword: 搜索关键字（小写）
            
        Returns:
            匹配分数
        """
        score = 0.0
        feature_name = feature['name'].lower()
        
        # 精确匹配：功能名完全等于关键字（权重 10）
        if feature_name == keyword:
            score += 10.0
        # 前缀匹配：功能名以关键字开头（权重 8）
        elif feature_name.startswith(keyword):
            score += 8.0
        # 包含匹配：功能名包含关键字（权重 6）
        elif keyword in feature_name:
            score += 6.0
        
        # 关键字匹配：metadata.keywords 中包含关键字（权重 5）
        keywords = feature.get('keywords', [])
        for kw in keywords:
            if keyword in kw.lower():
                score += 5.0
                break
        
        # 标题匹配：title 中包含关键字（权重 4）
        title = feature.get('title', '').lower()
        if keyword in title:
            score += 4.0
        
        # 描述匹配：description 中包含关键字（权重 3）
        description = feature.get('description', '').lower()
        if keyword in description:
            score += 3.0
        
        return score
    
    def _difficulty_rank(self, difficulty: str) -> int:
        """
        难度级别排序
        
        Args:
            difficulty: 难度级别
            
        Returns:
            排序权重（越小越优先）
        """
        difficulty_map = {
            'beginner': 1,
            'intermediate': 2,
            'advanced': 3
        }
        return difficulty_map.get(difficulty.lower(), 999)
