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

**方式一：pip安装**
```bash
pip install opendemo
```

**方式二：从源码安装**
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
opendemo config init

# 设置API密钥
opendemo config set ai.api_key YOUR_API_KEY
opendemo config set ai.api_endpoint YOUR_ENDPOINT
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

# 更多示例
opendemo get go prometheus       # 获取Prometheus监控demo
opendemo get go grpc             # 获取gRPC服务demo
opendemo get go health           # 获取健康检查demo
opendemo get nodejs cluster      # 获取Cluster集群demo
opendemo get nodejs jwt          # 获取JWT认证demo
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
opendemo new python 异步HTTP请求处理
opendemo new go 并发编程 --difficulty intermediate
opendemo new nodejs async-await --difficulty intermediate

# 第三方库Demo → 自动识别，输出到 libraries 目录
opendemo new python numpy           # → python/libraries/numpy/
opendemo new python requests HTTP请求       # → python/libraries/requests/
opendemo new python pandas 数据分析  # → python/libraries/pandas/
opendemo new java spring-boot web服务       # → java/libraries/spring-boot/
opendemo new go gin 中间件           # → go/libraries/gin/
opendemo new nodejs express 路由     # → nodejs/libraries/express/

# 普通编程主题（中文或标准库）输出到语言根目录
opendemo new python 数据处理               # → opendemo_output/python/
opendemo new python logging                 # → opendemo_output/python/ (标准库)

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
| **Python** | 76 | 基础语法(51) + 第三方库(numpy(25)) |
| **Go** | 92 | 基础语法、并发编程、DevOps/SRE、网络编程、工程实践 |
| **Node.js** | 67 | 基础语法、异步编程、DevOps/SRE、安全认证、工程实践 |
| **总计** | **235** | 多语言全覆盖 |

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

### 第三方库Demo - NumPy

| Demo名称 | 功能说明 | 测试状态 |
|---------|---------|----------|
| `aggregate-functions` | 聚合函数 (sum, mean, std) | ✅ 通过 |
| `array-concatenation` | 数组拼接分割 (concatenate, stack, split) | ✅ 通过 |
| `array-creation` | 数组创建 (zeros, ones, arange, linspace) | ✅ 通过 |
| `array-indexing` | 索引与切片 | ✅ 通过 |
| `array-reshape` | 数组形状操作 (reshape, transpose, flatten) | ✅ 通过 |
| `basic-math` | 基础数学运算 | ✅ 通过 |
| `bitwise-operations` | 位运算 | ✅ 通过 |
| `boolean-indexing` | 布尔索引/掩码 | ✅ 通过 |
| `broadcasting` | 广播机制 | ✅ 通过 |
| `datetime-operations` | 日期时间操作 | ✅ 通过 |
| `fft-transform` | 傅里叶变换 (FFT) | ✅ 通过 |
| `file-io` | 文件读写 (save, load, savetxt) | ✅ 通过 |
| `linear-algebra` | 线性代数 (特征值, 行列式, 逆矩阵) | ✅ 通过 |
| `logic-functions` | 逻辑函数 | ✅ 通过 |
| `masked-arrays` | 掩码数组 | ✅ 通过 |
| `matrix-multiplication` | 矩阵乘法 | ✅ 通过 |
| `polynomial` | 多项式操作 | ✅ 通过 |
| `random-generation` | 随机数生成 | ✅ 通过 |
| `set-operations` | 集合操作 | ✅ 通过 |
| `sorting-searching` | 排序与搜索 (sort, argsort) | ✅ 通过 |
| `statistics` | 统计函数 (mean, median, std) | ✅ 通过 |
| `string-operations` | 字符串操作 | ✅ 通过 |
| `structured-arrays` | 结构化数组 | ✅ 通过 |
| `universal-functions` | 通用函数 (ufunc) | ✅ 通过 |
| `window-functions` | 窗口函数 | ✅ 通过 |

**总计**: 25个Demo，覆盖NumPy核心功能，全部测试通过

### Python Demo完整清单 (76个)

<details>
<summary>点击展开Python Demo列表</summary>

**基础语法Demo (51个)**

| Demo名称 | 功能说明 |
|---------|----------|
| `abc-interfaces` | 抽象基类与接口 |
| `async-programming` | 异步编程 |
| `bitwise-operations` | 位运算 |
| `caching` | 缓存机制 |
| `cli-argparse` | 命令行参数解析 |
| `collections-module` | collections模块 |
| `comprehensions` | 推导式 |
| `config-management` | 配置管理 |
| `context-managers` | 上下文管理器 |
| `control-flow` | 控制流 |
| `copy-deepcopy` | 浅拷贝与深拷贝 |
| `database-sqlite` | SQLite数据库操作 |
| `dataclasses` | 数据类 |
| `datetime` | 日期时间处理 |
| `debugging` | 调试技巧 |
| `descriptors-property` | 描述符与属性 |
| `dict-operations` | 字典操作 |
| `enums` | 枚举类型 |
| `environment-variables` | 环境变量 |
| `exception-handling` | 异常处理 |
| `file-operations` | 文件操作 |
| `functions-decorators` | 函数与装饰器 |
| `functools-module` | functools模块 |
| `http-requests` | HTTP请求 |
| `inheritance-mro` | 继承与MRO |
| `iterators-generators` | 迭代器与生成器 |
| `itertools-module` | itertools模块 |
| `json-yaml` | JSON/YAML处理 |
| `lambda-expressions` | Lambda表达式 |
| `list-operations` | 列表操作 |
| `logging` | 日志记录 |
| `magic-methods` | 魔术方法 |
| `metaclasses` | 元类 |
| `modules-packages` | 模块与包 |
| `multiprocessing` | 多进程 |
| `multithreading` | 多线程 |
| `numbers-math` | 数字与数学 |
| `oop-classes` | 面向对象编程 |
| `operator-module` | operator模块 |
| `pathlib-os` | 路径与系统操作 |
| `profiling-optimization` | 性能分析与优化 |
| `regex` | 正则表达式 |
| `scope-closures` | 作用域与闭包 |
| `serialization-pickle` | 序列化pickle |
| `set-operations` | 集合操作 |
| `socket-networking` | Socket网络编程 |
| `string-operations` | 字符串操作 |
| `threading-synchronization` | 线程同步 |
| `tuple-basics` | 元组基础 |
| `type-hints` | 类型提示 |
| `unit-testing` | 单元测试 |

**第三方库Demo - NumPy (25个)**

| Demo名称 | 功能说明 | 路径 |
|---------|----------|------|
| `aggregate-functions` | 聚合函数 | libraries/numpy/ |
| `array-concatenation` | 数组拼接分割 | libraries/numpy/ |
| `array-creation` | 数组创建 | libraries/numpy/ |
| `array-indexing` | 索引与切片 | libraries/numpy/ |
| `array-reshape` | 数组形状操作 | libraries/numpy/ |
| `basic-math` | 基础数学运算 | libraries/numpy/ |
| `bitwise-operations` | 位运算 | libraries/numpy/ |
| `boolean-indexing` | 布尔索引/掩码 | libraries/numpy/ |
| `broadcasting` | 广播机制 | libraries/numpy/ |
| `datetime-operations` | 日期时间操作 | libraries/numpy/ |
| `fft-transform` | 傅里叶变换 | libraries/numpy/ |
| `file-io` | 文件读写 | libraries/numpy/ |
| `linear-algebra` | 线性代数 | libraries/numpy/ |
| `logic-functions` | 逻辑函数 | libraries/numpy/ |
| `masked-arrays` | 掩码数组 | libraries/numpy/ |
| `matrix-multiplication` | 矩阵乘法 | libraries/numpy/ |
| `polynomial` | 多项式操作 | libraries/numpy/ |
| `random-generation` | 随机数生成 | libraries/numpy/ |
| `set-operations` | 集合操作 | libraries/numpy/ |
| `sorting-searching` | 排序与搜索 | libraries/numpy/ |
| `statistics` | 统计函数 | libraries/numpy/ |
| `string-operations` | 字符串操作 | libraries/numpy/ |
| `structured-arrays` | 结构化数组 | libraries/numpy/ |
| `universal-functions` | 通用函数(ufunc) | libraries/numpy/ |
| `window-functions` | 窗口函数 | libraries/numpy/ |

</details>

### Go Demo完整清单 (92个)

<details>
<summary>点击展开Go Demo列表</summary>

| Demo名称 | 功能说明 |
|---------|----------|
| `go-cobra-cli-cli-tool-demo` | Cobra CLI工具 |
| `go-dockersdkgo-container-management` | Docker SDK容器管理 |
| `go-ginwebdemo-web-framework-intro` | Gin Web框架 |
| `go-go` | Go基础 |
| `go-go-badgerdb-demo-embedded-db-storage` | BadgerDB嵌入式存储 |
| `go-go-cache-warmup-strategy-demo` | 缓存预热策略 |
| `go-go-channels-demo` | Channel通道 |
| `go-go-consul-service-discovery` | Consul服务发现 |
| `go-go-context` | Context上下文 |
| `go-go-context-practice` | Context实践 |
| `go-go-control-flow-demo` | 控制流 |
| `go-go-db-connection-pool-demo` | 数据库连接池 |
| `go-go-defer-demo` | Defer延迟执行 |
| `go-go-demo` ~ `go-go-demo-15` | Go基础系列(16个) |
| `go-go-elkdemo-log-aggregation` | ELK日志聚合 |
| `go-go-embedded-programming-demo` | 嵌入式编程 |
| `go-go-embeddemo-embed-static-assets` | Embed静态资源 |
| `go-go-error-handling-demo` | 错误处理 |
| `go-go-http-demo` | HTTP编程 |
| `go-go-http-restful-api-demo` | RESTful API |
| `go-go-json-demo` | JSON处理 |
| `go-go-jwtdemo-auth-login-verify` | JWT认证 |
| `go-go-maps-demo` | Map映射 |
| `go-go-oauth20-third-party-login` | OAuth2.0第三方登录 |
| `go-go-panic-recover-demo` | Panic/Recover |
| `go-go-pprof-demo` | pprof性能分析 |
| `go-go-prometheus-metrics-demo` | Prometheus指标 |
| `go-go-protobuf-serialization-demo` | Protobuf序列化 |
| `go-go-redis-cache-operations-demo` | Redis缓存操作 |
| `go-go-redis-distributed-lock-demo` | Redis分布式锁 |
| `go-go-select-demo` | Select选择器 |
| `go-go-select-mechanism-demo` | Select机制 |
| `go-go-swagger-demo` | Swagger文档 |
| `go-go-tcp-network-programming` | TCP网络编程 |
| `go-go-variable-types-demo` | 变量类型 |
| `go-go-variables-types-demo` | 变量基础 |
| `go-go-viper-config-env-integration` | Viper配置管理 |
| `go-go-worker-pool-demo` | 工作池 |
| `go-gocontextdemo-timeout-context-demo` | Context超时 |
| `go-gocron-cron-scheduler-demo` | Cron定时任务 |
| `go-godemo` | Go示例 |
| `go-godemo-benchmark-profiling` | 基准测试 |
| `go-godemo-config-hot-reload-demo` | 配置热重载 |
| `go-godemo-dependency-injection-demo` | 依赖注入 |
| `go-godemo-exponential-backoff-retry` | 指数退避重试 |
| `go-godemo-functional-programming-practice` | 函数式编程 |
| `go-godemo-health-check-monitor` | 健康检查 |
| `go-godemo-load-balancer-reverse-proxy` | 负载均衡/反向代理 |
| `go-godemo-log-rotation-demo` | 日志轮转 |
| `go-godemo-signal-graceful-shutdown` | 优雅关闭 |
| `go-godemo-table-driven-testing` | 表驱动测试 |
| `go-godocker-multi-stage-docker-build` | Docker多阶段构建 |
| `go-gogoroutines-demo` | Goroutines基础 |
| `go-gogoroutines-goroutines-basics-demo` | Goroutines入门 |
| `go-gogoroutines-goroutines-basics-demo-1` | Goroutines入门2 |
| `go-gogoroutines-goroutines-detailed-demo` | Goroutines详解 |
| `go-gogoroutines-goroutines-practical-demo` | Goroutines实战 |
| `go-gohashjwt-crypto-hash-jwt-demo` | 加密哈希JWT |
| `go-gohttp-middleware-http-server` | HTTP中间件 |
| `go-goiota-const-enum-iota-demo` | iota常量枚举 |
| `go-goiota-const-enum-iota-usage` | iota用法 |
| `go-goiota-constants-enums-iota-demo` | 常量枚举 |
| `go-golrudemo-lru-cache-impl-demo` | LRU缓存实现 |
| `go-gomakefile-makefile-automation-demo` | Makefile自动化 |
| `go-gomutexwaitgroup-mutex-waitgroup-control-demo` | Mutex/WaitGroup控制 |
| `go-gomutexwaitgroup-mutex-waitgroup-demo` | Mutex/WaitGroup |
| `go-gomutexwaitgroup-mutex-waitgroup-demo-1` | Mutex/WaitGroup2 |
| `go-gorm-demo` | GORM ORM框架 |
| `go-goselect-mechanism-demo` | Select机制 |
| `go-gosql-sql-transaction-demo` | SQL事务 |
| `go-gozapdemo-structured-logging-zap-demo` | Zap结构化日志 |
| `go-grpc-protobuf-go-demo` | gRPC/Protobuf |
| `go-istiogo-service-mesh-proxy` | Istio服务网格 |
| `go-kafkago-producer-consumer` | Kafka生产消费 |
| `go-opentelemetrygo-distributed-tracing` | OpenTelemetry分布式追踪 |
| `go-rabbitmq-amqp-go-demo` | RabbitMQ AMQP |
| `go-websocket-gorilla-realtime-communication` | WebSocket实时通信 |

</details>

### Node.js Demo完整清单 (67个)

<details>
<summary>点击展开Node.js Demo列表</summary>

| Demo名称 | 功能说明 |
|---------|----------|
| `nodejs-arrow-functions-demo` | 箭头函数 |
| `nodejs-async-await-nodejs-demo` | Async/Await |
| `nodejs-axios-demo` | Axios HTTP客户端 |
| `nodejs-bullnodejs-demo-queue-async-tasks` | Bull任务队列 |
| `nodejs-consulnodejsdemo-service-discovery-config` | Consul服务发现 |
| `nodejs-docker-sdk-for-nodejs-container-management-demo` | Docker SDK容器管理 |
| `nodejs-express-restful-api-demo` | Express RESTful API |
| `nodejs-generator-async-flow-control-demo` | Generator异步控制 |
| `nodejs-graphql-api-demo` | GraphQL API |
| `nodejs-helmet-security-middleware-demo` | Helmet安全中间件 |
| `nodejs-ioredis-nodejs-demo` | ioredis Redis客户端 |
| `nodejs-jest-mockdemo-mock-unit-testing` | Jest Mock单元测试 |
| `nodejs-jwtnodejs-auth-authorization` | JWT认证授权 |
| `nodejs-kafkanodejs-producer-consumer` | Kafka生产消费 |
| `nodejs-mapsetdemo` | Map/Set数据结构 |
| `nodejs-multerdemo-file-upload-handling` | Multer文件上传 |
| `nodejs-nestjsdemo-framework-intro` | NestJS框架 |
| `nodejs-node-cron-cron-scheduler-demo` | Node-cron定时任务 |
| `nodejs-nodejs-buffer-demo` | Buffer缓冲区 |
| `nodejs-nodejs-class-inheritance-demo` | 类与继承 |
| `nodejs-nodejs-cluster-cluster-load-balancing` | Cluster集群负载均衡 |
| `nodejs-nodejs-demo` ~ `nodejs-nodejs-demo-10` | Node.js基础系列(11个) |
| `nodejs-nodejs-demo-regex-validation-demo` | 正则验证 |
| `nodejs-nodejs-filesystem-operations-demo` | 文件系统操作 |
| `nodejs-nodejs-health-check-demo` | 健康检查 |
| `nodejs-nodejs-http-demo` | HTTP编程 |
| `nodejs-nodejs-json-demo` | JSON处理 |
| `nodejs-nodejs-middleware-chain-demo` | 中间件链 |
| `nodejs-nodejs-mongodb-mongoose-demo` | MongoDB/Mongoose |
| `nodejs-nodejs-object-operations-demo` | 对象操作 |
| `nodejs-nodejs-osdemo-os-system-monitor` | OS系统监控 |
| `nodejs-nodejs-path-demo` | Path路径处理 |
| `nodejs-nodejs-prometheusdemo-metrics-collection` | Prometheus指标采集 |
| `nodejs-nodejs-promises-demo` | Promise异步 |
| `nodejs-nodejs-proxyreflect-demo` | Proxy/Reflect |
| `nodejs-nodejs-rate-limiter-demo` | 限流器 |
| `nodejs-nodejs-streams-demo` | Stream流 |
| `nodejs-nodejs-swagger-openapi-demo` | Swagger/OpenAPI |
| `nodejs-nodejs-variable-types-demo` | 变量类型 |
| `nodejs-nodejs-variables-basics-demo` | 变量基础 |
| `nodejs-nodejs-worker-threads-multithreading-demo` | Worker多线程 |
| `nodejs-nodejscrypto-hashbcrypt-crypto-bcrypt-demo` | Crypto加密哈希 |
| `nodejs-nodejsdemo-cron-scheduling` | Cron调度 |
| `nodejs-nodejsdemo-env-variables-demo` | 环境变量 |
| `nodejs-nodejsdemo-graceful-shutdown-demo` | 优雅关闭 |
| `nodejs-nodejsdemo-logging-management` | 日志管理 |
| `nodejs-nodejsdemo-retry-exponential-backoff` | 指数退避重试 |
| `nodejs-nodejsdemo-unit-testing-coverage` | 单元测试覆盖率 |
| `nodejs-nodejshttpdemo-load-balancer-proxy` | HTTP负载均衡代理 |
| `nodejs-oauth20passportnodejs-demo-passport-oauth-integration` | Passport OAuth |
| `nodejs-pm2nodejs-multi-process-deployment` | PM2多进程部署 |
| `nodejs-sequelize-orm-database-operations-demo` | Sequelize ORM |
| `nodejs-socketiodemo-realtime-chat-demo` | Socket.io实时聊天 |
| `nodejs-symbol-symbol-iterator-demo` | Symbol/Iterator |
| `nodejs-template-strings-demo` | 模板字符串 |
| `nodejs-typescript-express-api-demo` | TypeScript Express |
| `nodejs-websocket-realtime-communication` | WebSocket实时通信 |

</details>

### Demo目录结构

```
opendemo_output/
├── python/
│   ├── logging/              # 编程主题Demo
│   │   ├── metadata.json
│   │   ├── code/
│   │   └── requirements.txt
│   └── libraries/            # 第三方库Demo
│       └── numpy/            # NumPy库Demo
│           ├── array-creation/
│           ├── array-indexing/
│           ├── array-reshape/
│           ├── array-concatenation/
│           ├── basic-math/
│           ├── aggregate-functions/
│           ├── random-generation/
│           ├── sorting-searching/
│           ├── file-io/
│           └── fft-transform/
├── go/
│   ├── go-goroutines.../
│   └── libraries/
│       └── gin/
└── nodejs/
    ├── nodejs-express.../
    └── libraries/
        └── axios/
```

### Demo结构

每个Demo包含:
- `metadata.json`: Demo元数据
- `README.md`: 实操指南文档
- `code/`: 代码文件目录
- `requirements.txt` 或 `pom.xml` 或 `go.mod` 或 `package.json`: 依赖声明
- `tests/`: 测试文件(可选)

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
│   ├── __init__.py
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
│       ├── python/
│       ├── go/
│       ├── nodejs/
│       └── java/
├── scripts/                  # 工具脚本
│   ├── start.py              # 交互式启动脚本
│   └── ...                   # 其他脚本
├── data/                     # 数据文件目录
│   └── demo_mapping.json     # Demo映射配置
├── opendemo_output/          # Demo输出目录
│   ├── python/
│   │   ├── libraries/        # 第三方库Demo
│   │   └── <普通主题demo>/   # 编程主题Demo
│   ├── go/
│   │   └── libraries/
│   └── nodejs/
│       └── libraries/
├── tests/                    # 测试文件
├── pyproject.toml            # 项目配置
└── README.md                 # 本文件
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
|------|--------|----|--------|
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

### 设置开发环境

```bash
git clone https://github.com/opendemo/opendemo.git
cd opendemo
pip install -e ".[dev]"
```

### 交互式启动（可选）

如果你更喜欢菜单式的交互方式，可以使用交互式启动脚本：

```bash
python scripts/start.py
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

## 贡献

欢迎贡献! 请查看贡献指南了解详情。

---

## 许可证

本项目采用 **MIT License** 开源许可证。

---

## 联系方式

- **问题反馈**: [GitHub Issues](https://github.com/opendemo/opendemo/issues)
- **项目仓库**: https://github.com/opendemo/opendemo
