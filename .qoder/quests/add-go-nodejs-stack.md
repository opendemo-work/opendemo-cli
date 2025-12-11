# 新增 Go 和 Node.js 技术栈设计文档

## 需求概述

在 Open Demo CLI 项目中新增对 Go 语言和 Node.js 的支持，通过 AI 生成并验证相关语言的核心概念 Demo，扩充项目的多语言覆盖能力。

## 设计目标

- 在 `opendemo_output` 目录下新增 `go` 和 `nodejs` 两个语言目录
- 使用 `opendemo new` 命令批量生成 Go 和 Node.js 的核心概念 Demo
- 对生成的 Demo 进行可执行性验证
- 确保生成的 Demo 符合项目标准结构和质量要求

## 系统影响范围

### 代码修改

| 模块 | 文件路径 | 修改内容 | 修改原因 |
|------|---------|---------|---------|
| CLI入口 | opendemo/cli.py | 更新 SUPPORTED_LANGUAGES 常量 | 添加 'go' 和 'nodejs' 到支持语言列表 |
| 验证器 | opendemo/core/verifier.py | 新增 Go 和 Node.js 验证方法 | 支持新语言的可执行性验证 |

### 目录结构变化

新增输出目录结构：

```
opendemo_output/
├── python/        (已存在，51个 demo)
├── go/            (新增)
│   ├── variables-types/
│   ├── functions/
│   ├── goroutines-channels/
│   └── ...
└── nodejs/        (新增)
    ├── variables-types/
    ├── functions/
    ├── async-await/
    └── ...
```

## Go 语言核心概念清单

基于 Go 语言特性，建议生成以下核心概念 Demo（共约 25-30 个）：

### 基础语法类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| 变量与类型 | variables types | beginner | 变量声明、基本类型、类型推断 |
| 常量与枚举 | constants enums iota | beginner | 常量定义、iota 枚举 |
| 控制流 | control-flow if-switch-for | beginner | 条件语句、循环结构 |
| 数组与切片 | arrays slices | beginner | 数组、切片操作和内存模型 |
| 映射 | maps | beginner | map 的创建、操作、遍历 |
| 字符串处理 | strings | beginner | 字符串操作、格式化 |

### 函数与方法类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| 函数基础 | functions | beginner | 函数定义、多返回值、参数传递 |
| 方法与接收者 | methods receivers | intermediate | 值接收者、指针接收者 |
| 闭包 | closures | intermediate | 闭包概念和应用 |
| 延迟调用 | defer | beginner | defer 语句的使用和执行顺序 |

### 并发编程类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| Goroutine | goroutines | intermediate | 协程创建和使用 |
| Channel | channels | intermediate | 通道的创建、发送、接收 |
| Select | select | intermediate | select 多路复用 |
| 同步原语 | sync mutex waitgroup | intermediate | sync 包的使用 |
| Context | context | intermediate | 上下文控制和取消 |

### 接口与类型系统类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| 结构体 | structs | beginner | 结构体定义、嵌套、标签 |
| 接口 | interfaces | intermediate | 接口定义、实现、类型断言 |
| 空接口 | empty-interface | intermediate | interface{} 和泛型使用 |
| 类型嵌入 | embedding | intermediate | 结构体嵌入、方法提升 |
| 泛型 | generics | advanced | Go 1.18+ 泛型特性 |

### 错误处理类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| 错误处理 | error-handling | beginner | error 接口、错误返回 |
| Panic 与 Recover | panic recover | intermediate | 异常处理机制 |
| 自定义错误 | custom-errors | intermediate | 实现 error 接口 |

### 包与模块类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| 包管理 | packages | beginner | 包的定义、导入、可见性 |
| Go Modules | go-modules | beginner | go.mod 模块管理 |

### 标准库类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| 文件操作 | file-io | beginner | 文件读写、os 包 |
| JSON 处理 | json | beginner | JSON 序列化和反序列化 |
| HTTP 客户端 | http-client | intermediate | net/http 客户端 |
| HTTP 服务器 | http-server | intermediate | HTTP 服务器构建 |
| 时间处理 | time | beginner | time 包的使用 |
| 正则表达式 | regex | intermediate | regexp 包 |

### 测试类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| 单元测试 | testing | beginner | testing 包、表格驱动测试 |
| 基准测试 | benchmarking | intermediate | 性能测试 |

## Node.js 核心概念清单

基于 Node.js 和现代 JavaScript/TypeScript 特性，建议生成以下核心概念 Demo（共约 25-30 个）：

### 基础语法类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| 变量与类型 | variables types | beginner | var/let/const、基本类型 |
| 解构赋值 | destructuring | beginner | 对象和数组解构 |
| 模板字符串 | template-strings | beginner | 模板字面量 |
| 箭头函数 | arrow-functions | beginner | 箭头函数语法和 this 绑定 |
| 扩展运算符 | spread-operator | beginner | 展开语法和剩余参数 |

### 函数类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| 函数基础 | functions | beginner | 函数声明、表达式、回调 |
| 高阶函数 | higher-order-functions | intermediate | map、filter、reduce |
| 闭包 | closures | intermediate | 闭包和作用域 |
| 柯里化 | currying | intermediate | 函数柯里化 |

### 异步编程类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| 回调函数 | callbacks | beginner | 回调模式和回调地狱 |
| Promise | promises | intermediate | Promise 链式调用 |
| Async/Await | async-await | intermediate | 异步函数语法 |
| Event Loop | event-loop | advanced | 事件循环机制 |
| EventEmitter | event-emitter | intermediate | 事件发射器模式 |

### 模块系统类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| CommonJS | commonjs require | beginner | require/module.exports |
| ES Modules | es-modules import | beginner | import/export 语法 |
| NPM 包管理 | npm package-json | beginner | package.json、依赖管理 |

### 核心模块类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| 文件系统 | fs file-system | beginner | fs 模块文件操作 |
| 路径处理 | path | beginner | path 模块 |
| Buffer | buffer | intermediate | Buffer 缓冲区操作 |
| Stream | streams | intermediate | 流处理：Readable/Writable |
| HTTP 模块 | http-module | intermediate | 原生 HTTP 服务器 |
| 进程管理 | process child-process | intermediate | process 和 child_process |

### Web 框架类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| Express 基础 | express-basics | intermediate | Express 框架入门 |
| 中间件 | middleware | intermediate | Express 中间件机制 |
| RESTful API | restful-api | intermediate | REST API 设计 |

### 数据处理类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| JSON 处理 | json | beginner | JSON.parse/stringify |
| 数组方法 | array-methods | beginner | 数组常用方法 |
| 对象操作 | object-operations | beginner | Object 方法 |

### 现代特性类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| 类与继承 | classes inheritance | intermediate | ES6 类语法 |
| 生成器 | generators | advanced | Generator 函数 |
| Symbol | symbols | intermediate | Symbol 类型 |
| Proxy | proxy | advanced | Proxy 和 Reflect |
| Map 与 Set | map-set | beginner | Map、Set 数据结构 |

### 工具类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| 调试技巧 | debugging | beginner | console、debugger |
| 环境变量 | environment-variables | beginner | process.env、dotenv |
| 错误处理 | error-handling | intermediate | try/catch、自定义错误 |

## 实施流程设计

### 阶段一：环境准备

| 步骤 | 操作内容 | 验证标准 |
|------|---------|---------|
| 1.1 更新语言支持列表 | 修改 cli.py 中 SUPPORTED_LANGUAGES | 'go' 和 'nodejs' 已添加到列表 |
| 1.2 创建输出目录 | 手动或自动创建 opendemo_output/go 和 opendemo_output/nodejs | 目录存在且可写 |
| 1.3 验证 AI API 配置 | 确认 OpenAI API 密钥已配置 | opendemo config get ai.api_key 返回有效值 |

### 阶段二：扩展验证器

为支持 Go 和 Node.js 的验证，需要扩展验证器功能。

#### Go 验证逻辑设计

验证器需要执行以下步骤：

| 步骤序号 | 验证步骤 | 具体操作 | 成功条件 |
|---------|---------|---------|---------|
| 1 | 检查 Go 环境 | 执行 `go version` 命令 | 返回码为 0 且输出包含版本号 |
| 2 | 复制到临时目录 | 将 demo 复制到临时工作空间 | 文件完整复制 |
| 3 | 初始化模块 | 如有 go.mod 则跳过，否则执行 `go mod init demo` | go.mod 文件存在 |
| 4 | 安装依赖 | 执行 `go mod tidy` | 返回码为 0 |
| 5 | 编译检查 | 执行 `go build ./...` | 编译成功，无错误输出 |
| 6 | 运行代码 | 执行 `go run code/*.go` 或 `go run .` | 返回码为 0，无运行时错误 |

#### Node.js 验证逻辑设计

验证器需要执行以下步骤：

| 步骤序号 | 验证步骤 | 具体操作 | 成功条件 |
|---------|---------|---------|---------|
| 1 | 检查 Node 环境 | 执行 `node --version` | 返回码为 0 且输出包含版本号 |
| 2 | 复制到临时目录 | 将 demo 复制到临时工作空间 | 文件完整复制 |
| 3 | 安装依赖 | 如有 package.json，执行 `npm install` | 返回码为 0 或无 package.json |
| 4 | 运行代码 | 执行 `node code/main.js` 或 package.json 中的 start 脚本 | 返回码为 0，无运行时错误 |

#### 验证器方法签名

```
验证器类新增方法:

_verify_go(demo_path: Path) -> Dict[str, Any]
  输入: Demo 路径
  输出: 验证结果字典，包含 verified、method、steps、outputs、errors 字段
  
_verify_nodejs(demo_path: Path) -> Dict[str, Any]
  输入: Demo 路径
  输出: 验证结果字典，包含 verified、method、steps、outputs、errors 字段

verify(demo_path: Path, language: str) -> Dict[str, Any]
  修改: 添加对 'go' 和 'nodejs' 语言的分支判断
```

### 阶段三：批量生成 Demo

使用脚本或手动方式批量调用 `opendemo new` 命令生成 Demo。

#### 批量生成脚本设计

脚本功能职责：
- 读取预定义的概念清单
- 逐个调用 opendemo new 命令
- 根据配置决定是否启用验证
- 记录生成结果（成功/失败）
- 生成汇总报告

脚本执行逻辑：

```
对于每个语言 (Go, Node.js):
  对于每个核心概念:
    1. 构造命令: opendemo new <language> <topic> --difficulty <level> [--verify]
    2. 执行命令并捕获输出
    3. 解析结果状态
    4. 记录到日志文件
    5. 如果失败，记录错误信息并继续下一个
  生成语言级别汇总报告
生成总体汇总报告
```

#### 生成参数配置

| 配置项 | 说明 | 建议值 |
|--------|------|--------|
| 难度级别 | 每个概念的难度 | 参考概念清单表格 |
| 启用验证 | 是否在生成后验证 | 建议启用（--verify） |
| 失败重试 | 失败时是否重试 | 建议重试 1-2 次 |
| 批处理大小 | 每批生成数量 | 建议 5-10 个一批，避免 API 限流 |
| 间隔时间 | 每个请求间隔 | 建议 2-5 秒，避免 API 限流 |

### 阶段四：验证与质量检查

生成完成后，需要进行质量检查。

#### 验证维度

| 维度 | 检查项 | 检查方法 | 合格标准 |
|------|--------|---------|---------|
| 结构完整性 | 目录结构 | 检查是否包含 metadata.json、README.md、code/ | 所有必需文件存在 |
| 元数据正确性 | metadata.json 内容 | 验证语言、关键字、描述字段 | 字段完整且正确 |
| 代码可执行性 | 执行验证 | 运行验证器 | verified 为 true |
| 文档质量 | README.md 内容 | 检查是否包含说明、示例、运行步骤 | 内容完整且格式正确 |
| 依赖声明 | requirements.txt / package.json / go.mod | 检查依赖文件存在性和有效性 | 如有依赖，文件格式正确 |

#### 批量验证流程

```
验证流程：
1. 扫描 opendemo_output/go 和 opendemo_output/nodejs 目录
2. 对每个 demo 执行：
   a. 结构完整性检查
   b. 元数据有效性检查
   c. 如未验证过，执行验证器
3. 统计验证结果：
   - 总数
   - 成功数
   - 失败数
   - 失败原因分类
4. 生成验证报告
```

### 阶段五：问题修复与重新生成

对于验证失败的 Demo，需要进行分析和修复。

#### 故障分类与处理策略

| 故障类型 | 可能原因 | 处理策略 |
|---------|---------|---------|
| AI 生成失败 | API 限流、网络问题、提示词问题 | 重新生成，增加重试间隔 |
| 编译失败 | 代码语法错误、依赖缺失 | 检查生成代码质量，可能需要调整提示词或手动修复 |
| 运行失败 | 运行时错误、逻辑错误 | 分析错误日志，手动修复或重新生成 |
| 环境问题 | Go/Node.js 未安装、版本不兼容 | 确认运行环境，安装必要工具 |
| 依赖问题 | 依赖包不可用、版本冲突 | 修正依赖声明文件 |

#### 修复流程

```
对于每个失败的 demo:
  1. 查看错误日志和类型
  2. 分析根本原因
  3. 判断修复策略:
     - 如果是临时性问题（网络、限流）：延迟后重试
     - 如果是代码质量问题：考虑重新生成或手动修复
     - 如果是环境问题：修复环境配置
  4. 执行修复操作
  5. 重新验证
  6. 更新记录
```

### 阶段六：最终验证与任务关闭

确保所有 Demo 都已成功生成并验证。

#### 完成标准

| 标准项 | 要求 | 验证方法 |
|--------|------|---------|
| Demo 数量 | Go 和 Node.js 各生成至少 20 个核心概念 Demo | 统计目录数量 |
| 验证通过率 | 至少 90% 的 Demo 验证通过 | 统计验证结果 |
| 文档完整性 | 所有 Demo 包含完整的 README 和元数据 | 批量检查 |
| 可执行性 | 通过验证的 Demo 可以按照 README 指引成功运行 | 随机抽样测试 |

#### 最终检查清单

```
完成前检查：
□ opendemo_output/go 目录存在且包含至少 20 个 demo
□ opendemo_output/nodejs 目录存在且包含至少 20 个 demo
□ 所有 demo 包含 metadata.json、README.md、code/ 目录
□ 验证通过率达标（>=90%）
□ SUPPORTED_LANGUAGES 已更新为 ['python', 'java', 'go', 'nodejs']
□ 验证器已实现 _verify_go 和 _verify_nodejs 方法
□ 生成汇总报告已完成
□ 所有修改已提交代码仓库
```

## Demo 标准结构规范

每个生成的 Demo 应遵循以下标准结构：

### 目录结构

```
<language>/<demo-name>/
├── metadata.json       # 元数据文件
├── README.md          # 实操指南文档
├── code/              # 代码文件目录
│   └── <main-file>   # 主文件（Go: main.go, Node.js: main.js）
└── <deps-file>       # 依赖声明文件（Go: go.mod, Node.js: package.json）
```

### metadata.json 结构

```
必需字段:
- name: demo 名称
- language: 编程语言 (go 或 nodejs)
- keywords: 关键字数组
- description: 简短描述
- difficulty: 难度级别 (beginner/intermediate/advanced)
- author: 作者信息
- created_at: 创建时间 (ISO 8601 格式)
- updated_at: 更新时间 (ISO 8601 格式)
- version: 版本号
- verified: 是否已验证 (boolean)

可选字段:
- dependencies: 依赖信息
```

### README.md 内容要求

应包含以下部分：
1. 简介：概念说明和学习目标
2. 环境要求：运行所需的工具和版本
3. 快速开始：安装依赖和运行步骤
4. 代码说明：核心代码解析
5. 扩展学习：相关资源链接

### 代码文件要求

- Go: 包含完整的 package 声明，代码可独立编译运行
- Node.js: 使用现代 JavaScript/ES6+ 语法，代码清晰易懂
- 包含必要的注释说明核心概念
- 输出应清晰展示概念的使用效果

## 风险与约束

### 技术风险

| 风险项 | 影响 | 应对措施 |
|--------|------|---------|
| AI 生成质量不稳定 | 部分 Demo 代码可能无法运行 | 启用验证机制，失败后重新生成 |
| API 限流 | 生成速度受限 | 分批生成，设置请求间隔 |
| Go/Node.js 环境依赖 | 验证需要本地环境支持 | 确认运行环境或在文档中说明环境要求 |
| 生成的依赖包失效 | 依赖包可能不存在或版本冲突 | 使用稳定的依赖版本，验证时检测 |

### 资源约束

| 约束项 | 说明 | 影响 |
|--------|------|------|
| AI API 调用成本 | 生成 50+ Demo 需要大量 API 调用 | 需要预估成本，优化生成策略 |
| 时间成本 | 批量生成和验证耗时较长 | 需合理安排时间，可分阶段完成 |
| 验证环境要求 | 需要 Go 和 Node.js 运行时环境 | 确保开发机器已安装相关工具 |

### 质量约束

| 约束项 | 要求 | 保障措施 |
|--------|------|---------|
| 代码质量 | 生成的代码应遵循语言最佳实践 | 在 AI 提示词中强调代码质量要求 |
| 文档质量 | README 应详细且易懂 | 验证时检查文档完整性 |
| 概念覆盖 | 应覆盖核心和常用概念 | 参考概念清单表格，确保覆盖面 |

## 成功标准

任务完成需满足以下条件：

1. **语言支持扩展完成**
   - SUPPORTED_LANGUAGES 包含 'go' 和 'nodejs'
   - 验证器实现了对应语言的验证方法

2. **Demo 生成完成**
   - opendemo_output/go 目录包含至少 20 个 Go Demo
   - opendemo_output/nodejs 目录包含至少 20 个 Node.js Demo

3. **验证通过**
   - 至少 90% 的 Demo 通过可执行性验证
   - 所有 Demo 结构完整，包含必需文件

4. **文档完整**
   - 每个 Demo 包含详细的 README.md
   - metadata.json 信息准确完整

5. **任务记录**
   - 生成过程记录完整
   - 验证报告已生成
   - 问题和解决方案已记录

## 实施建议

### 分批执行策略

建议将任务分为多个批次执行：

| 批次 | 内容 | 数量 | 优先级 |
|------|------|------|--------|
| 批次 1 | Go 基础语法 + Node.js 基础语法 | 各 6-8 个 | 高 |
| 批次 2 | Go 并发编程 + Node.js 异步编程 | 各 5-6 个 | 高 |
| 批次 3 | Go 接口与类型 + Node.js 核心模块 | 各 5-6 个 | 中 |
| 批次 4 | Go 标准库 + Node.js 工具类 | 各 3-5 个 | 中 |
| 批次 5 | 补充和高级主题 | 按需 | 低 |

### 质量优先原则

在生成过程中：
- 优先保证 Demo 的质量而非数量
- 验证失败的 Demo 应分析原因并修复
- 必要时手动调整生成的代码以确保质量
- 关键概念的 Demo 应特别重视

### 工具支持建议

可以编写辅助脚本或工具来提高效率：
- 批量生成脚本：自动化调用 opendemo new 命令
- 验证检查脚本：批量检查 Demo 结构和元数据
- 报告生成工具：自动统计和生成汇总报告
- 概念清单管理：使用配置文件管理要生成的概念列表

## 后续扩展方向

完成 Go 和 Node.js 支持后，可以考虑：
- 为其他流行语言添加支持（如 Rust、TypeScript、Java 等）
- 丰富每个语言的 Demo 覆盖范围
- 建立 Demo 质量评分机制
- 支持多语言 Demo 的交叉对比学习
- 构建自动化的 Demo 质量检测和更新流程
| 单元测试 | testing | beginner | testing 包、表格驱动测试 |
| 基准测试 | benchmarking | intermediate | 性能测试 |

## Node.js 核心概念清单

基于 Node.js 和现代 JavaScript/TypeScript 特性，建议生成以下核心概念 Demo（共约 25-30 个）：

### 基础语法类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| 变量与类型 | variables types | beginner | var/let/const、基本类型 |
| 解构赋值 | destructuring | beginner | 对象和数组解构 |
| 模板字符串 | template-strings | beginner | 模板字面量 |
| 箭头函数 | arrow-functions | beginner | 箭头函数语法和 this 绑定 |
| 扩展运算符 | spread-operator | beginner | 展开语法和剩余参数 |

### 函数类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| 函数基础 | functions | beginner | 函数声明、表达式、回调 |
| 高阶函数 | higher-order-functions | intermediate | map、filter、reduce |
| 闭包 | closures | intermediate | 闭包和作用域 |
| 柯里化 | currying | intermediate | 函数柯里化 |

### 异步编程类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| 回调函数 | callbacks | beginner | 回调模式和回调地狱 |
| Promise | promises | intermediate | Promise 链式调用 |
| Async/Await | async-await | intermediate | 异步函数语法 |
| Event Loop | event-loop | advanced | 事件循环机制 |
| EventEmitter | event-emitter | intermediate | 事件发射器模式 |

### 模块系统类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| CommonJS | commonjs require | beginner | require/module.exports |
| ES Modules | es-modules import | beginner | import/export 语法 |
| NPM 包管理 | npm package-json | beginner | package.json、依赖管理 |

### 核心模块类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| 文件系统 | fs file-system | beginner | fs 模块文件操作 |
| 路径处理 | path | beginner | path 模块 |
| Buffer | buffer | intermediate | Buffer 缓冲区操作 |
| Stream | streams | intermediate | 流处理：Readable/Writable |
| HTTP 模块 | http-module | intermediate | 原生 HTTP 服务器 |
| 进程管理 | process child-process | intermediate | process 和 child_process |

### Web 框架类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| Express 基础 | express-basics | intermediate | Express 框架入门 |
| 中间件 | middleware | intermediate | Express 中间件机制 |
| RESTful API | restful-api | intermediate | REST API 设计 |

### 数据处理类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| JSON 处理 | json | beginner | JSON.parse/stringify |
| 数组方法 | array-methods | beginner | 数组常用方法 |
| 对象操作 | object-operations | beginner | Object 方法 |

### 现代特性类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| 类与继承 | classes inheritance | intermediate | ES6 类语法 |
| 生成器 | generators | advanced | Generator 函数 |
| Symbol | symbols | intermediate | Symbol 类型 |
| Proxy | proxy | advanced | Proxy 和 Reflect |
| Map 与 Set | map-set | beginner | Map、Set 数据结构 |

### 工具类

| 概念 | 主题关键字 | 难度 | 说明 |
|------|-----------|------|------|
| 调试技巧 | debugging | beginner | console、debugger |
| 环境变量 | environment-variables | beginner | process.env、dotenv |
| 错误处理 | error-handling | intermediate | try/catch、自定义错误 |

## 实施流程设计

### 阶段一：环境准备

| 步骤 | 操作内容 | 验证标准 |
|------|---------|---------|
| 1.1 更新语言支持列表 | 修改 cli.py 中 SUPPORTED_LANGUAGES | 'go' 和 'nodejs' 已添加到列表 |
| 1.2 创建输出目录 | 手动或自动创建 opendemo_output/go 和 opendemo_output/nodejs | 目录存在且可写 |
| 1.3 验证 AI API 配置 | 确认 OpenAI API 密钥已配置 | opendemo config get ai.api_key 返回有效值 |

### 阶段二：扩展验证器

为支持 Go 和 Node.js 的验证，需要扩展验证器功能。

#### Go 验证逻辑设计

验证器需要执行以下步骤：

| 步骤序号 | 验证步骤 | 具体操作 | 成功条件 |
|---------|---------|---------|---------|
| 1 | 检查 Go 环境 | 执行 `go version` 命令 | 返回码为 0 且输出包含版本号 |
| 2 | 复制到临时目录 | 将 demo 复制到临时工作空间 | 文件完整复制 |
| 3 | 初始化模块 | 如有 go.mod 则跳过，否则执行 `go mod init demo` | go.mod 文件存在 |
| 4 | 安装依赖 | 执行 `go mod tidy` | 返回码为 0 |
| 5 | 编译检查 | 执行 `go build ./...` | 编译成功，无错误输出 |
| 6 | 运行代码 | 执行 `go run code/*.go` 或 `go run .` | 返回码为 0，无运行时错误 |

#### Node.js 验证逻辑设计

验证器需要执行以下步骤：

| 步骤序号 | 验证步骤 | 具体操作 | 成功条件 |
|---------|---------|---------|---------|
| 1 | 检查 Node 环境 | 执行 `node --version` | 返回码为 0 且输出包含版本号 |
| 2 | 复制到临时目录 | 将 demo 复制到临时工作空间 | 文件完整复制 |
| 3 | 安装依赖 | 如有 package.json，执行 `npm install` | 返回码为 0 或无 package.json |
| 4 | 运行代码 | 执行 `node code/main.js` 或 package.json 中的 start 脚本 | 返回码为 0，无运行时错误 |

#### 验证器方法签名

```
验证器类新增方法:

_verify_go(demo_path: Path) -> Dict[str, Any]
  输入: Demo 路径
  输出: 验证结果字典，包含 verified、method、steps、outputs、errors 字段
  
_verify_nodejs(demo_path: Path) -> Dict[str, Any]
  输入: Demo 路径
  输出: 验证结果字典，包含 verified、method、steps、outputs、errors 字段

verify(demo_path: Path, language: str) -> Dict[str, Any]
  修改: 添加对 'go' 和 'nodejs' 语言的分支判断
```

### 阶段三：批量生成 Demo

使用脚本或手动方式批量调用 `opendemo new` 命令生成 Demo。

#### 批量生成脚本设计

脚本功能职责：
- 读取预定义的概念清单
- 逐个调用 opendemo new 命令
- 根据配置决定是否启用验证
- 记录生成结果（成功/失败）
- 生成汇总报告

脚本执行逻辑：

```
对于每个语言 (Go, Node.js):
  对于每个核心概念:
    1. 构造命令: opendemo new <language> <topic> --difficulty <level> [--verify]
    2. 执行命令并捕获输出
    3. 解析结果状态
    4. 记录到日志文件
    5. 如果失败，记录错误信息并继续下一个
  生成语言级别汇总报告
生成总体汇总报告
```

#### 生成参数配置

| 配置项 | 说明 | 建议值 |
|--------|------|--------|
| 难度级别 | 每个概念的难度 | 参考概念清单表格 |
| 启用验证 | 是否在生成后验证 | 建议启用（--verify） |
| 失败重试 | 失败时是否重试 | 建议重试 1-2 次 |
| 批处理大小 | 每批生成数量 | 建议 5-10 个一批，避免 API 限流 |
| 间隔时间 | 每个请求间隔 | 建议 2-5 秒，避免 API 限流 |

### 阶段四：验证与质量检查

生成完成后，需要进行质量检查。

#### 验证维度

| 维度 | 检查项 | 检查方法 | 合格标准 |
|------|--------|---------|---------|
| 结构完整性 | 目录结构 | 检查是否包含 metadata.json、README.md、code/ | 所有必需文件存在 |
| 元数据正确性 | metadata.json 内容 | 验证语言、关键字、描述字段 | 字段完整且正确 |
| 代码可执行性 | 执行验证 | 运行验证器 | verified 为 true |
| 文档质量 | README.md 内容 | 检查是否包含说明、示例、运行步骤 | 内容完整且格式正确 |
| 依赖声明 | requirements.txt / package.json / go.mod | 检查依赖文件存在性和有效性 | 如有依赖，文件格式正确 |

#### 批量验证流程

```
验证流程：
1. 扫描 opendemo_output/go 和 opendemo_output/nodejs 目录
2. 对每个 demo 执行：
   a. 结构完整性检查
   b. 元数据有效性检查
   c. 如未验证过，执行验证器
3. 统计验证结果：
   - 总数
   - 成功数
   - 失败数
   - 失败原因分类
4. 生成验证报告
```

### 阶段五：问题修复与重新生成

对于验证失败的 Demo，需要进行分析和修复。

#### 故障分类与处理策略

| 故障类型 | 可能原因 | 处理策略 |
|---------|---------|---------|
| AI 生成失败 | API 限流、网络问题、提示词问题 | 重新生成，增加重试间隔 |
| 编译失败 | 代码语法错误、依赖缺失 | 检查生成代码质量，可能需要调整提示词或手动修复 |
| 运行失败 | 运行时错误、逻辑错误 | 分析错误日志，手动修复或重新生成 |
| 环境问题 | Go/Node.js 未安装、版本不兼容 | 确认运行环境，安装必要工具 |
| 依赖问题 | 依赖包不可用、版本冲突 | 修正依赖声明文件 |

#### 修复流程

```
对于每个失败的 demo:
  1. 查看错误日志和类型
  2. 分析根本原因
  3. 判断修复策略:
     - 如果是临时性问题（网络、限流）：延迟后重试
     - 如果是代码质量问题：考虑重新生成或手动修复
     - 如果是环境问题：修复环境配置
  4. 执行修复操作
  5. 重新验证
  6. 更新记录
```

### 阶段六：最终验证与任务关闭

确保所有 Demo 都已成功生成并验证。

#### 完成标准

| 标准项 | 要求 | 验证方法 |
|--------|------|---------|
| Demo 数量 | Go 和 Node.js 各生成至少 20 个核心概念 Demo | 统计目录数量 |
| 验证通过率 | 至少 90% 的 Demo 验证通过 | 统计验证结果 |
| 文档完整性 | 所有 Demo 包含完整的 README 和元数据 | 批量检查 |
| 可执行性 | 通过验证的 Demo 可以按照 README 指引成功运行 | 随机抽样测试 |

#### 最终检查清单

```
完成前检查：
□ opendemo_output/go 目录存在且包含至少 20 个 demo
□ opendemo_output/nodejs 目录存在且包含至少 20 个 demo
□ 所有 demo 包含 metadata.json、README.md、code/ 目录
□ 验证通过率达标（>=90%）
□ SUPPORTED_LANGUAGES 已更新为 ['python', 'java', 'go', 'nodejs']
□ 验证器已实现 _verify_go 和 _verify_nodejs 方法
□ 生成汇总报告已完成
□ 所有修改已提交代码仓库
```

## Demo 标准结构规范

每个生成的 Demo 应遵循以下标准结构：

### 目录结构

```
<language>/<demo-name>/
├── metadata.json       # 元数据文件
├── README.md          # 实操指南文档
├── code/              # 代码文件目录
│   └── <main-file>   # 主文件（Go: main.go, Node.js: main.js）
└── <deps-file>       # 依赖声明文件（Go: go.mod, Node.js: package.json）
```

### metadata.json 结构

```
必需字段:
- name: demo 名称
- language: 编程语言 (go 或 nodejs)
- keywords: 关键字数组
- description: 简短描述
- difficulty: 难度级别 (beginner/intermediate/advanced)
- author: 作者信息
- created_at: 创建时间 (ISO 8601 格式)
- updated_at: 更新时间 (ISO 8601 格式)
- version: 版本号
- verified: 是否已验证 (boolean)

可选字段:
- dependencies: 依赖信息
```

### README.md 内容要求

应包含以下部分：
1. 简介：概念说明和学习目标
2. 环境要求：运行所需的工具和版本
3. 快速开始：安装依赖和运行步骤
4. 代码说明：核心代码解析
5. 扩展学习：相关资源链接

### 代码文件要求

- Go: 包含完整的 package 声明，代码可独立编译运行
- Node.js: 使用现代 JavaScript/ES6+ 语法，代码清晰易懂
- 包含必要的注释说明核心概念
- 输出应清晰展示概念的使用效果

## 风险与约束

### 技术风险

| 风险项 | 影响 | 应对措施 |
|--------|------|---------|
| AI 生成质量不稳定 | 部分 Demo 代码可能无法运行 | 启用验证机制，失败后重新生成 |
| API 限流 | 生成速度受限 | 分批生成，设置请求间隔 |
| Go/Node.js 环境依赖 | 验证需要本地环境支持 | 确认运行环境或在文档中说明环境要求 |
| 生成的依赖包失效 | 依赖包可能不存在或版本冲突 | 使用稳定的依赖版本，验证时检测 |

### 资源约束

| 约束项 | 说明 | 影响 |
|--------|------|------|
| AI API 调用成本 | 生成 50+ Demo 需要大量 API 调用 | 需要预估成本，优化生成策略 |
| 时间成本 | 批量生成和验证耗时较长 | 需合理安排时间，可分阶段完成 |
| 验证环境要求 | 需要 Go 和 Node.js 运行时环境 | 确保开发机器已安装相关工具 |

### 质量约束

| 约束项 | 要求 | 保障措施 |
|--------|------|---------|
| 代码质量 | 生成的代码应遵循语言最佳实践 | 在 AI 提示词中强调代码质量要求 |
| 文档质量 | README 应详细且易懂 | 验证时检查文档完整性 |
| 概念覆盖 | 应覆盖核心和常用概念 | 参考概念清单表格，确保覆盖面 |

## 成功标准

任务完成需满足以下条件：

1. **语言支持扩展完成**
   - SUPPORTED_LANGUAGES 包含 'go' 和 'nodejs'
   - 验证器实现了对应语言的验证方法

2. **Demo 生成完成**
   - opendemo_output/go 目录包含至少 20 个 Go Demo
   - opendemo_output/nodejs 目录包含至少 20 个 Node.js Demo

3. **验证通过**
   - 至少 90% 的 Demo 通过可执行性验证
   - 所有 Demo 结构完整，包含必需文件

4. **文档完整**
   - 每个 Demo 包含详细的 README.md
   - metadata.json 信息准确完整

5. **任务记录**
   - 生成过程记录完整
   - 验证报告已生成
   - 问题和解决方案已记录

## 实施建议

### 分批执行策略

建议将任务分为多个批次执行：

| 批次 | 内容 | 数量 | 优先级 |
|------|------|------|--------|
| 批次 1 | Go 基础语法 + Node.js 基础语法 | 各 6-8 个 | 高 |
| 批次 2 | Go 并发编程 + Node.js 异步编程 | 各 5-6 个 | 高 |
| 批次 3 | Go 接口与类型 + Node.js 核心模块 | 各 5-6 个 | 中 |
| 批次 4 | Go 标准库 + Node.js 工具类 | 各 3-5 个 | 中 |
| 批次 5 | 补充和高级主题 | 按需 | 低 |

### 质量优先原则

在生成过程中：
- 优先保证 Demo 的质量而非数量
- 验证失败的 Demo 应分析原因并修复
- 必要时手动调整生成的代码以确保质量
- 关键概念的 Demo 应特别重视

### 工具支持建议

可以编写辅助脚本或工具来提高效率：
- 批量生成脚本：自动化调用 opendemo new 命令
- 验证检查脚本：批量检查 Demo 结构和元数据
- 报告生成工具：自动统计和生成汇总报告
- 概念清单管理：使用配置文件管理要生成的概念列表

## 后续扩展方向

完成 Go 和 Node.js 支持后，可以考虑：
- 为其他流行语言添加支持（如 Rust、TypeScript、Java 等）
- 丰富每个语言的 Demo 覆盖范围
- 建立 Demo 质量评分机制
- 支持多语言 Demo 的交叉对比学习
- 构建自动化的 Demo 质量检测和更新流程
