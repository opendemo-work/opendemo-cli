# n8n 案例

## 简介

本案例展示如何在 Kubernetes 集群中部署 n8n，一个强大的开源自动化工具，用于创建工作流和自动化任务。

## 功能说明

**n8n 工作流平台**：在 Kubernetes 集群中部署完整的 n8n 系统，用于创建和管理自动化工作流

**难度**：intermediate

**功能覆盖**：
- ✅ 工作流创建与管理
- ✅ 节点集成
- ✅ 触发器配置
- ✅ 数据处理
- ✅ API 接口
- ✅ 监控与告警

## 配置文件

- `n8n-deployment.yaml` - n8n 部署配置
- `n8n-service.yaml` - n8n 服务暴露配置
- `configmap.yaml` - 配置管理
- `secret.yaml` - 密钥管理
- `rbac.yaml` - 权限控制
- `metadata.json` - 案例元数据

## 部署步骤

### 1. 准备工作

- Kubernetes 集群 (v1.23+)
- Helm 3.0+
- 持久存储 (PV/PVC)
- 域名（可选，用于 Ingress 配置）

### 2. 部署 n8n

```bash
# 1. 配置密钥
kubectl create secret generic n8n-secrets \
  --from-literal=n8n-encryption-key=YOUR_ENCRYPTION_KEY \
  --from-literal=postgres-password=YOUR_POSTGRES_PASSWORD \
  --namespace n8n-system

# 2. 部署 n8n
kubectl apply -f rbac.yaml
kubectl apply -f configmap.yaml
kubectl apply -f n8n-deployment.yaml
kubectl apply -f n8n-service.yaml

# 3. 验证部署
kubectl get pods -n n8n-system
kubectl get svc -n n8n-system
```

### 3. 访问 n8n

```bash
# 获取服务地址
N8N_SERVICE_IP=$(kubectl get svc n8n-service -n n8n-system -o jsonpath='{.status.loadBalancer.ingress[0].ip}')

# 访问 n8n 界面
echo "n8n 界面地址: http://$N8N_SERVICE_IP:5678"

# 测试 API
curl -X GET http://$N8N_SERVICE_IP:5678/api/v1/workflows
```

## 架构说明

### 核心组件

1. **n8n 核心**：工作流引擎和 Web 界面
2. **数据库**：存储工作流、执行历史等数据
3. **队列**：管理任务执行
4. **存储**：保存文件和数据

### 数据流

1. 用户创建工作流 → 保存到数据库
2. 触发器触发 → 执行工作流 → 处理数据 → 保存执行结果

## 监控与维护

### 监控指标

- n8n 服务响应时间
- 工作流执行成功率
- 队列长度
- 资源使用情况

### 日志管理

- n8n 服务日志
- 工作流执行日志
- 错误日志

### 常见问题

| 问题 | 解决方案 |
|------|----------|
| 数据库连接失败 | 检查数据库配置和网络连接 |
| 工作流执行失败 | 检查工作流配置和节点设置 |
| 资源不足 | 调整部署的资源请求和限制 |
| 持久存储问题 | 检查 PVC 配置和存储提供商 |

## 版本兼容性

- Kubernetes v1.23.x+ 完全兼容
- Kubernetes v1.24.x+ 完全兼容
- Kubernetes v1.25.x+ 完全兼容
- Kubernetes v1.26.x+ 完全兼容
- Kubernetes v1.27.x+ 完全兼容
- Kubernetes v1.28.x+ 完全兼容
- Kubernetes v1.29.x+ 完全兼容

## 相关资源

- [n8n 官方文档](https://docs.n8n.io/)
- [n8n GitHub 仓库](https://github.com/n8n-io/n8n)
- [Kubernetes 官方文档](https://kubernetes.io/docs/)

## 许可证

MIT License