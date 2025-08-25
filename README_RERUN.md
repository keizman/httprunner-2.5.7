# HttpRunner 2.5.7 with Rerun Feature

基于 HttpRunner 2.5.7 添加了失败重试功能的增强版本，专为减少环境干扰造成的用例执行失败而设计。

## 🚀 新增特性

### 1. Testcase 级别的 Rerun 机制
- 使用 `--rerun N` 参数在 testcase 失败后重新运行指定次数
- **重要**: 只针对 testcase 级别，不会重跑整个 testsuite
- 智能重试：只重跑失败的测试步骤，成功的步骤不会重复执行

### 2. 增强的测试报告
- 显示重跑次数信息：`重跑: 1/3`（表示设置了3次重跑，实际重跑了1次）
- 更新为 light 主题的测试报告
- 添加饼状图显示用例执行结果占比
- 悬浮显示详细数值，默认显示成功率百分比

### 3. 优化的用户体验
- 只保留最终结果，避免重复的错误信息干扰
- 详细的重试日志，便于调试和跟踪

## 📦 安装方法

### 方法1: 直接从 GitHub 安装 (推荐)
```bash
pip install git+https://github.com/keizman/httprunner-2.5.7.git
```

### 方法2: 指定分支安装
```bash
pip install git+https://github.com/keizman/httprunner-2.5.7.git@master
```

### 方法3: 升级现有安装
```bash
pip install --upgrade git+https://github.com/keizman/httprunner-2.5.7.git
```

### 方法4: 在 requirements.txt 中使用
```txt
git+https://github.com/keizman/httprunner-2.5.7.git
```

## 🔧 使用示例

### 基本用法
```bash
# 运行测试用例，失败时重跑3次
hrun testcase.yaml --rerun 3

# 查看帮助信息
hrun --help | grep rerun
```

### 测试用例示例
```yaml
config:
    name: API Test with Rerun
    base_url: http://api.example.com

teststeps:
    - name: Get user info
      request:
          method: GET
          url: /users/123
      validate:
          - check: status_code
            assert: equals
            expect: 200
    
    - name: Update user
      request:
          method: POST
          url: /users/123
          json:
              name: "New Name"
      validate:
          - check: status_code
            assert: equals
            expect: 200
```

运行命令：
```bash
hrun api_test.yaml --rerun 2
```

## 📊 报告特性

### 重跑信息显示
测试报告中会显示：
```
通过: 15 ; 失败: 2 ; 错误: 0 ; 跳过: 0 ; 重跑: 1/2
```

### 饼状图功能
- **测试步骤图表**: 显示所有步骤的成功/失败比例
- **测试用例图表**: 显示用例级别的成功/失败比例
- **交互功能**: 
  - 默认显示成功率百分比 (如: `85.5%`)
  - 鼠标悬浮显示具体数值 (如: `17/20`)

## 🛠️ 开发和贡献

### 本地开发安装
```bash
git clone https://github.com/keizman/httprunner-2.5.7.git
cd httprunner-2.5.7
pip install -e .
```

### 构建分发包
```bash
# 使用提供的构建脚本
./build_package.sh

# 或手动构建
python setup.py sdist bdist_wheel
```

### 验证安装
```bash
# 检查版本
hrun --version

# 检查rerun参数
hrun --help | grep rerun

# 运行验证脚本
./verify_installation.sh
```

## 📋 系统要求

- Python >= 2.7 (推荐 Python 3.6+)
- 支持 Linux, macOS, Windows
- 依赖包会自动安装

## 🔄 从原版 HttpRunner 迁移

如果您之前使用的是原版 HttpRunner 2.5.7，可以直接升级：

```bash
# 卸载原版
pip uninstall httprunner

# 安装增强版
pip install git+https://github.com/keizman/httprunner-2.5.7.git
```

所有原有的测试用例和功能保持完全兼容，只是新增了 `--rerun` 功能。

## 📝 更新日志

### 2025-08-22
- ✅ 添加 testcase 级别的 rerun 机制
- ✅ 测试报告添加 rerun 次数显示
- ✅ 更换为 light 主题测试报告
- ✅ 添加用例统计饼状图和成功/失败比例信息

## 📞 支持与反馈

如有问题或建议，请：
1. 提交 [GitHub Issue](https://github.com/keizman/httprunner-2.5.7/issues)
2. 查看 [使用文档](PACKAGING_GUIDE.md)

---

**注意**: 这是基于 HttpRunner 2.5.7 的增强版本，添加了企业级的失败重试功能，特别适合在不稳定网络环境中进行API自动化测试。