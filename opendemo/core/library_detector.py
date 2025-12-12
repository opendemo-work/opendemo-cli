"""
库检测器模块

负责识别命令中的库名，区分库命令和普通主题命令。
"""

import json
from pathlib import Path
from typing import Optional, Dict, Any, List
from opendemo.utils.logger import get_logger

logger = get_logger(__name__)


class LibraryDetector:
    """库检测器类"""
    
    def __init__(self, storage_service, ai_service=None):
        """
        初始化库检测器
        
        Args:
            storage_service: 存储服务实例
            ai_service: AI服务实例（可选，用于智能判断库名）
        """
        self.storage = storage_service
        self.ai_service = ai_service
        self._supported_libraries_cache = {}
    
    def is_library_command(self, language: str, keywords: List[str]) -> bool:
        """
        判断是否为库命令
        
        Args:
            language: 编程语言
            keywords: 关键字列表
            
        Returns:
            是否为库命令
        """
        if not keywords:
            return False
        
        # 获取第一个关键字作为潜在的库名
        potential_library = keywords[0].lower()
        
        # 检查是否在支持的库列表中
        supported_libraries = self.get_supported_libraries(language)
        return potential_library in supported_libraries
    
    def parse_library_command(
        self,
        language: str,
        keywords: List[str]
    ) -> Optional[Dict[str, Any]]:
        """
        解析库命令，返回库名和功能名
        
        Args:
            language: 编程语言
            keywords: 关键字列表
            
        Returns:
            库命令信息字典，包含 library、feature 等字段；非库命令返回 None
        """
        if not self.is_library_command(language, keywords):
            return None
        
        library_name = keywords[0].lower()
        feature_keywords = keywords[1:] if len(keywords) > 1 else []
        
        # 加载库元数据
        library_metadata = self.load_library_metadata(language, library_name)
        
        if not library_metadata:
            logger.warning(f"Library metadata not found for {language}/{library_name}")
            return None
        
        return {
            'library': library_name,
            'language': language,
            'feature_keywords': feature_keywords,
            'metadata': library_metadata
        }
    
    def get_supported_libraries(self, language: str) -> List[str]:
        """
        获取支持的库列表
        
        Args:
            language: 编程语言
            
        Returns:
            库名列表
        """
        # 检查缓存
        if language in self._supported_libraries_cache:
            return self._supported_libraries_cache[language]
        
        libraries = []
        
        # 从内置库目录扫描
        builtin_library_path = self.storage.builtin_library_path / language.lower() / 'libraries'
        if builtin_library_path.exists():
            for item in builtin_library_path.iterdir():
                if item.is_dir() and not item.name.startswith('_'):
                    # 检查是否有 _library.json 文件
                    if (item / '_library.json').exists():
                        libraries.append(item.name)
        
        # 从用户库目录扫描
        user_library_path = self.storage.user_library_path / language.lower() / 'libraries'
        if user_library_path.exists():
            for item in user_library_path.iterdir():
                if item.is_dir() and not item.name.startswith('_'):
                    if (item / '_library.json').exists() and item.name not in libraries:
                        libraries.append(item.name)
        
        # 缓存结果
        self._supported_libraries_cache[language] = libraries
        logger.info(f"Found {len(libraries)} libraries for {language}: {libraries}")
        
        return libraries
    
    def load_library_metadata(
        self,
        language: str,
        library: str
    ) -> Optional[Dict[str, Any]]:
        """
        加载库的元数据
        
        Args:
            language: 编程语言
            library: 库名称
            
        Returns:
            库元数据字典，失败返回 None
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
    
    def clear_cache(self):
        """清除缓存"""
        self._supported_libraries_cache.clear()
    
    def looks_like_library_name(self, keyword: str) -> bool:
        """
        判断关键字是否看起来像库名
        
        库名特征：
        - 单个单词（无空格）
        - 全小写或带连字符/下划线
        - 不包含中文
        - 长度适中（2-30字符）
        
        Args:
            keyword: 待检测的关键字
            
        Returns:
            是否看起来像库名
        """
        if not keyword:
            return False
        
        # 转小写
        kw = keyword.lower().strip()
        
        # 长度检查
        if len(kw) < 2 or len(kw) > 30:
            return False
        
        # 不能包含中文字符
        for char in kw:
            if '\u4e00' <= char <= '\u9fff':
                return False
        
        # 只允许字母、数字、连字符、下划线
        allowed_chars = set('abcdefghijklmnopqrstuvwxyz0123456789-_')
        if not all(c in allowed_chars for c in kw):
            return False
        
        # 必须以字母开头
        if not kw[0].isalpha():
            return False
        
        return True
    
    def detect_library_for_new_command(
        self,
        language: str,
        keywords: List[str],
        use_ai: bool = True
    ) -> Optional[str]:
        """
        为 new 命令检测库名（即使库尚未注册）
        
        如果第一个关键字看起来像库名，则返回它作为库名。
        当 AI 服务可用时，会使用 AI 进行更智能的判断。
        
        Args:
            language: 编程语言
            keywords: 关键字列表
            use_ai: 是否使用AI判断（默认True）
            
        Returns:
            检测到的库名，或 None
        """
        if not keywords:
            return None
        
        first_keyword = keywords[0]
        
        # 先检查是否在已知库列表中
        supported_libraries = self.get_supported_libraries(language)
        if first_keyword.lower() in supported_libraries:
            return first_keyword.lower()
        
        # 使用 AI 进行智能判断
        if use_ai and self.ai_service:
            result = self.ai_service.classify_keyword(language, first_keyword)
            
            if result.get('is_library') and result.get('confidence', 0) >= 0.5:
                library_name = result.get('library_name') or first_keyword.lower()
                logger.info(
                    f"AI detected '{first_keyword}' as library: {library_name} "
                    f"(confidence: {result.get('confidence', 0):.2f})"
                )
                return library_name
            else:
                logger.info(
                    f"AI detected '{first_keyword}' as topic, not library "
                    f"(confidence: {result.get('confidence', 0):.2f})"
                )
                return None
        
        # 回退到启发式检测
        if self.looks_like_library_name(first_keyword):
            logger.info(f"Heuristic detected potential library name: {first_keyword}")
            return first_keyword.lower()
        
        return None
