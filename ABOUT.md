# Open Demo CLI

> 智能化编程学习辅助CLI工具 - 快速获取高质量、可执行的Demo代码

---

## 目录

- [项目简介](#项目简介)
- [快速开始](#快速开始)
- [命令详解](#命令详解)
- [Demo库](#demo库)
- [配置管理](#配置管理)
- [项目结构](#项目结构)
- [技术架构](#技术架构)
- [测试与质量](#测试与质量)
- [常见问题](#常见问题)
- [开发指南](#开发指南)
- [许可证](#许可证)

---

## 项目简介

Open Demo CLI 是一个帮助开发者快速获取编程语言Demo代码的命令行工具。

### 核心特性

| 特性 | 说明 |
|------|------|
| 🚀 **快速获取** | 通过简单命令获取完整示例代码 |
| 📚 **AI智能生成** | 本地未找到时自动调用AI生成 |
| 📦 **第三方库支持** | AI智能识别第三方库，自动组织到libraries目录 |
| ✅ **可选验证** | 自动验证生成代码的可执行性 |
| 🔍 **智能搜索** | 快速搜索本地Demo库 |
| 🌍 **社区贡献** | 支持将优质Demo贡献到公共库 |

### 支持的语言

| 语言 | Demo数量 | 特色 |
|------|---------|------|
| Python | 51 | 基础语法、并发、标准库、网络 |
| Go | 89 | 含完整DevOps/SRE支持 |
| Node.js | 67 | 含完整DevOps/SRE支持 |
| Java | 待扩充 | - |
| **总计** | **207** | 多语言全覆盖 |

---

## 快速开始

### 安装

```bash
# 克隆项目
git clone https://github.com/opendemo/opendemo.git
cd opendemo

# 安装
pip install -e .
```

### 验证安装

```bash
python -m opendemo.cli --help
```

### 配置AI服务（可选）

```bash
# 初始化配置
python -m opendemo.cli config init

# 设置API密钥
python -m opendemo.cli config set ai.api_key YOUR_API_KEY
python -m opendemo.cli config set ai.api_endpoint YOUR_ENDPOINT
```

### 基础用法

```bash
# 搜索Demo
opendemo search python              # 列出所有Python Demo
opendemo search go                  # 列出所有Go Demo
opendemo search python async        # 按关键字过滤

# 获取Demo
opendemo get python logging         # 获取已有Demo
opendemo get go goroutines          # 获取Go并发Demo
opendemo get nodejs express         # 获取Express框架Demo

# 创建新Demo
opendemo new python 网络爬虫        # 编程主题
opendemo new python numpy           # 第三方库（自动识别）
opendemo new go gin 中间件           # 指定库+主题
```

---

## 命令详解

### 命令概览

| 命令 | 功能 | 示例 |
|------|------|------|
| `search` | 搜索Demo | `opendemo search python` |
| `get` | 获取Demo | `opendemo get python logging` |
| `new` | 创建新Demo | `opendemo new python 装饰器` |
| `config` | 配置管理 | `opendemo config list` |

### search - 搜索Demo

```bash
# 查看支持的语言
opendemo search

# 列出特定语言的Demo
opendemo search python
opendemo search go
opendemo search nodejs

# 关键字过滤
opendemo search python async
opendemo search go prometheus
```

**输出示例：**
```
可用的语言:
  - python: 51 个demo
  - go: 89 个demo
  - nodejs: 67 个demo

找到 51 个匹配的demo:
╭───┬───────────────────┬────────┬──────────────────┬──────────╮
│ # │ 名称              │ 语言   │ 关键字           │ 难度     │
├───┼───────────────────┼────────┼──────────────────┼──────────┤
│ 1 │ async-programming │ python │ async            │ beginner │
│ 2 │ logging           │ python │ logging          │ beginner │
╰───┴───────────────────┴────────┴──────────────────┴──────────╯
```

### get - 获取Demo

**匹配优先级：**
1. **精确匹配** - 关键字完全等于文件夹名称
2. **语义匹配** - 关键字被包含在文件夹名称中
3. **AI生成** - 本地未找到时调用AI生成

```bash
# 精确匹配
opendemo get python logging

# 语义匹配 (list → list-operations)
opendemo get python list

# 强制重新生成
opendemo get python logging new
```

**输出示例：**
```
>>> 搜索 python - logging 的demo...
[OK] 在输出目录中找到匹配的demo: logging

名称: logging
路径: opendemo_output/python/logging

包含文件:
  - code/logging_demo.py

快速开始:
  1. cd opendemo_output/python/logging
  2. python code/logging_demo.py
```

### new - 创建新Demo

```bash
# 编程主题Demo → 输出到语言根目录
opendemo new python 网络爬虫
opendemo new go 并发编程 --difficulty intermediate

# 第三方库Demo → 自动识别，输出到 libraries 目录
opendemo new python numpy           # → python/libraries/numpy/
opendemo new python pandas 数据分析  # → python/libraries/pandas/
opendemo new go gin 中间件           # → go/libraries/gin/
opendemo new nodejs express 路由     # → nodejs/libraries/express/

# 带验证
opendemo new python 异步IO --verify
```

**第三方库智能识别规则：**
- 第三方库：numpy, pandas, requests, flask, gin, express 等
- 标准库模块：logging, os, json 等 → 视为编程主题
- 中文关键字：数据处理、异步编程 等 → 视为编程主题

### config - 配置管理

```bash
# 初始化配置
opendemo config init

# 查看配置
opendemo config list
opendemo config get ai.model

# 设置配置
opendemo config set ai.api_key sk-xxx
opendemo config set enable_verification true
```

---

## Demo库

### Demo统计

| 语言 | 数量 | 分类 |
|------|------|------|
| **Python** | 51 | 基础语法、数据类型、函数与类、高级特性、并发编程、标准库、文件IO、网络、调试测试 |
| **Go** | 89 | 基础语法(15+)、并发编程(12+)、DevOps/SRE(25+)、网络编程(12+)、工程实践(18+) |
| **Node.js** | 67 | 基础语法(15+)、异步编程(10+)、DevOps/SRE(20+)、安全认证(8+)、工程实践(14+) |

### DevOps/SRE Demo亮点

**Go语言：**
- Prometheus指标采集、健康检查、限流熔断、优雅关闭
- gRPC服务、Kafka/RabbitMQ消息队列、Docker SDK
- OpenTelemetry分布式追踪、Consul服务发现
- Gin/GORM、JWT/OAuth2.0、Swagger

**Node.js：**
- Express/NestJS框架、Cluster多进程、PM2部署
- 健康检查、优雅关闭、Prometheus监控
- JWT认证、Kafka消息队列、Docker SDK
- Socket.io实时通信、GraphQL API

### Demo目录结构

```
opendemo_output/
├── python/
│   ├── logging/              # 编程主题Demo
│   │   ├── metadata.json
│   │   ├── code/
│   │   └── requirements.txt
│   └── libraries/            # 第三方库Demo
│       ├── numpy/
│       └── pandas/
├── go/
│   ├── go-goroutines.../
│   └── libraries/
│       └── gin/
└── nodejs/
    ├── nodejs-express.../
    └── libraries/
        └── axios/
```

### 运行Demo

**Python:**
```bash
cd opendemo_output/python/logging
pip install -r requirements.txt
python code/logging_demo.py
```

**Go:**
```bash
cd opendemo_output/go/go-goroutines
go run .
```

**Node.js:**
```bash
cd opendemo_output/nodejs/nodejs-express
npm install
node code/main.js
```

---

## 配置管理

### 配置文件位置

| 类型 | 路径 |
|------|------|
| 全局配置 | `~/.opendemo/config.yaml` |
| 项目配置 | `./.opendemo.yaml` |

### 主要配置项

| 配置项 | 说明 | 默认值 |
|--------|------|--------|
| `output_directory` | Demo输出目录 | `./opendemo_output` |
| `user_demo_library` | 用户Demo库路径 | `~/.opendemo/demos` |
| `default_language` | 默认编程语言 | `python` |
| `enable_verification` | 是否启用自动验证 | `false` |
| `ai.provider` | AI服务提供商 | `openai` |
| `ai.api_key` | API密钥 | - |
| `ai.api_endpoint` | API端点URL | OpenAI默认 |
| `ai.model` | 使用的模型 | `gpt-4` |
| `ai.temperature` | 温度参数 | `0.7` |
| `ai.max_tokens` | 最大token数 | `4000` |

---

## 项目结构

```
opendemo/
├── opendemo/                 # 主包
│   ├── cli.py                # CLI入口
│   ├── core/                 # 核心业务逻辑
│   │   ├── demo_manager.py   # Demo管理器
│   │   ├── search_engine.py  # 搜索引擎
│   │   ├── generator.py      # 生成器
│   │   ├── verifier.py       # 验证器
│   │   ├── library_detector.py # 库名检测器
│   │   ├── library_manager.py  # 库管理器
│   │   └── contribution.py   # 贡献管理
│   ├── services/             # 服务层
│   │   ├── ai_service.py     # AI服务
│   │   ├── config_service.py # 配置服务
│   │   └── storage_service.py # 存储服务
│   ├── utils/                # 工具模块
│   │   ├── formatters.py     # 输出格式化
│   │   └── logger.py         # 日志工具
│   └── builtin_demos/        # 内置Demo库
├── opendemo_output/          # Demo输出目录
├── scripts/                  # 批量生成脚本
├── tests/                    # 测试文件
├── pyproject.toml            # 项目配置
└── ABOUT.md                  # 本文件
```

---

## 技术架构

### 架构设计

```
CLI层 → 业务逻辑层 → 服务层 → 数据层
```

| 层级 | 模块 | 职责 |
|------|------|------|
| CLI层 | cli.py | Click框架实现命令行界面 |
| 业务逻辑层 | core/ | Demo管理、搜索、生成、验证 |
| 服务层 | services/ | AI服务、配置服务、存储服务 |
| 数据层 | 文件系统 | Demo库、配置文件 |

### 技术栈

| 技术 | 用途 |
|------|------|
| Python 3.8+ | 核心语言 |
| Click | CLI框架 |
| Rich | 彩色输出美化 |
| PyYAML | 配置管理 |
| Requests | HTTP请求 |
| OpenAI API | AI代码生成 |

### 核心模块

| 模块 | 功能 |
|------|------|
| **ConfigService** | 全局/项目配置管理，YAML存储 |
| **StorageService** | 双层Demo库架构，文件系统抽象 |
| **DemoManager** | Demo加载/保存，元数据管理 |
| **SearchEngine** | 关键字匹配，相关性评分 |
| **AIService** | OpenAI API集成，Prompt构建，关键字分类 |
| **DemoVerifier** | 虚拟环境隔离，依赖安装，代码执行验证 |
| **LibraryDetector** | AI智能识别第三方库，启发式回退 |

### 验证器实现

**Go验证流程：**
```
环境检查(go version) → 模块初始化(go mod init) 
→ 依赖管理(go mod tidy) → 编译检查(go build) → 运行验证(go run)
```

**Node.js验证流程：**
```
环境检查(node --version) → 依赖安装(npm install) 
→ 智能主文件查找 → 运行验证(node/npm start)
```

---

## 测试与质量

### 单元测试

| 测试模块 | 用例数 | 状态 |
|---------|--------|------|
| test_config_service.py | 10 | ✅ 通过 |
| test_demo_manager.py | 10 | ✅ 通过 |
| test_search_engine.py | 13 | ✅ 通过 |
| **总计** | **33** | **✅ 全部通过** |

### 代码质量

| 检查项 | 状态 |
|--------|------|
| 语法检查 | ✅ 所有17个Python文件通过 |
| 静态分析 | ✅ 无编译错误、类型错误 |
| 模块导入 | ✅ CLI和核心模块正常 |
| 异常处理 | ✅ 使用`except Exception:`规范 |

### CLI功能测试

| 功能 | Python | Go | Node.js |
|------|--------|----|---------|
| search命令 | ✅ | ✅ | ✅ |
| get命令 | ✅ | ✅ | ✅ |
| new命令 | ✅ | ✅ | ✅ |
| 匹配逻辑 | ✅ | ✅ | ✅ |

### 批量生成工具

| 脚本 | Demo数量 | 用途 |
|------|---------|------|
| generate_minimal_demos.py | 40 | 快速验证 |
| quick_generate.py | 44 | 快速生成 |
| generate_demos.py | 49 | 完整生成 |

---

## 常见问题

### Q1: 如何使用AI生成功能？

配置API密钥和端点：
```bash
opendemo config set ai.api_key YOUR_KEY
opendemo config set ai.api_endpoint YOUR_ENDPOINT
```

### Q2: Demo保存在哪里？

- **编程主题Demo**：`opendemo_output/<语言>/<主题名>/`
- **第三方库Demo**：`opendemo_output/<语言>/libraries/<库名>/`

### Q3: 如何运行验证？

```bash
# 全局启用
opendemo config set enable_verification true

# 单次验证
opendemo new python 装饰器 --verify
```

### Q4: 搜索结果为空？

1. 确认Demo目录存在
2. 确认Demo有`metadata.json`文件
3. 尝试更宽泛的关键字

### Q5: 验证环境要求？

- Go：安装`go`命令
- Node.js：安装`node`和`npm`命令

---

## 开发指南

### 开发环境

```bash
git clone https://github.com/opendemo/opendemo.git
cd opendemo
pip install -e ".[dev]"
```

### 运行测试

```bash
python -m pytest tests/
```

### 代码格式化

```bash
black opendemo/
```

### 添加新语言支持

1. 在`cli.py`中添加到`SUPPORTED_LANGUAGES`
2. 在`verifier.py`中实现`_verify_<language>()`方法
3. 在`builtin_demos/`下创建对应目录

### 扩展计划

| 阶段 | 计划 |
|------|------|
| 短期 v1.x | Java支持、更多配置选项 |
| 中期 v2.x | Web界面、TypeScript/Rust、IDE插件 |
| 长期 v3.x+ | 智能推荐、多模态支持、企业版 |

---

## 许可证

本项目采用 **MIT License** 开源许可证。

---

## 文档说明

| 文档 | 说明 |
|------|------|
| **ABOUT.md** | 完整项目文档（本文件） |
| README.md | 项目简介（GitHub入口） |
| LICENSE | MIT开源许可证 |

---

## 联系方式

- **问题反馈**: [GitHub Issues](https://github.com/opendemo/opendemo/issues)
- **项目仓库**: https://github.com/opendemo/opendemo

---

*最后更新: 2025-12-12*
