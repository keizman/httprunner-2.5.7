# HttpRunner 2.5.7 Validate 对比项完整文档

## 概述

HttpRunner 2.5.7 提供了丰富的 validate 对比项，用于验证 API 响应结果。本文档列出了所有可用的对比项及其使用方法。

## 对比项分类

### 1. 相等性对比

#### `eq` / `equals` / `==` / `is`
**功能**: 断言完全相等  
**说明**: 检查实际值与期望值是否完全相等（使用 `==` 操作符）

```yaml
validate:
  - eq: [status_code, 200]
  - equals: [content.code, 0]
  - "==": [content.message, "success"]
  - is: [content.data.status, true]
```

#### `ne` / `not_equals`
**功能**: 断言不相等  
**说明**: 检查实际值与期望值是否不相等（使用 `!=` 操作符）

```yaml
validate:
  - ne: [status_code, 404]
  - not_equals: [content.error, null]
```

#### `str_eq` / `string_equals`
**功能**: 断言字符串相等  
**说明**: 将两个值都转换为字符串后进行比较

```yaml
validate:
  - str_eq: [content.user_id, "12345"]
  - string_equals: [headers.content-type, "application/json"]
```

### 2. 数值大小对比

#### `lt` / `less_than`
**功能**: 断言小于  
**说明**: 检查实际值是否小于期望值（使用 `<` 操作符）

```yaml
validate:
  - lt: [content.count, 100]
  - less_than: [elapsed.total_seconds, 2.0]
```

#### `le` / `less_than_or_equals`
**功能**: 断言小于等于  
**说明**: 检查实际值是否小于等于期望值（使用 `<=` 操作符）

```yaml
validate:
  - le: [content.page_size, 50]
  - less_than_or_equals: [content.score, 100]
```

#### `gt` / `greater_than`
**功能**: 断言大于  
**说明**: 检查实际值是否大于期望值（使用 `>` 操作符）

```yaml
validate:
  - gt: [content.total, 0]
  - greater_than: [content.timestamp, 1609459200]
```

#### `ge` / `greater_than_or_equals`
**功能**: 断言大于等于  
**说明**: 检查实际值是否大于等于期望值（使用 `>=` 操作符）

```yaml
validate:
  - ge: [content.age, 18]
  - greater_than_or_equals: [content.balance, 0]
```

### 3. 长度对比

#### `len_eq` / `length_equals` / `count_eq`
**功能**: 断言长度相等  
**说明**: 检查实际值的长度是否等于期望值

```yaml
validate:
  - len_eq: [content.items, 5]
  - length_equals: [content.username, 8]
  - count_eq: [content.tags, 3]
```

#### `len_gt` / `count_gt` / `length_greater_than` / `count_greater_than`
**功能**: 断言长度大于  
**说明**: 检查实际值的长度是否大于期望值

```yaml
validate:
  - len_gt: [content.description, 10]
  - length_greater_than: [content.items, 0]
```

#### `len_ge` / `count_ge` / `length_greater_than_or_equals` / `count_greater_than_or_equals`
**功能**: 断言长度大于等于  
**说明**: 检查实际值的长度是否大于等于期望值

```yaml
validate:
  - len_ge: [content.password, 6]
  - length_greater_than_or_equals: [content.results, 1]
```

#### `len_lt` / `count_lt` / `length_less_than` / `count_less_than`
**功能**: 断言长度小于  
**说明**: 检查实际值的长度是否小于期望值

```yaml
validate:
  - len_lt: [content.title, 100]
  - length_less_than: [content.errors, 1]
```

#### `len_le` / `count_le` / `length_less_than_or_equals` / `count_less_than_or_equals`
**功能**: 断言长度小于等于  
**说明**: 检查实际值的长度是否小于等于期望值

```yaml
validate:
  - len_le: [content.comment, 500]
  - length_less_than_or_equals: [content.warnings, 0]
```

### 4. 包含关系对比

#### `contains`
**功能**: 断言包含  
**说明**: 检查实际值是否包含期望值（适用于列表、元组、字典、字符串）

```yaml
validate:
  - contains: [content.tags, "python"]
  - contains: [content.permissions, "read"]
  - contains: [content.message, "success"]
```

#### `contained_by`
**功能**: 断言被包含  
**说明**: 检查实际值是否被期望值包含

```yaml
validate:
  - contained_by: [content.status, ["active", "pending", "inactive"]]
  - contained_by: ["admin", content.roles]
```

### 5. 字符串匹配对比

#### `startswith`
**功能**: 断言以指定字符串开头  
**说明**: 检查实际值是否以期望值开头

```yaml
validate:
  - startswith: [content.url, "https://"]
  - startswith: [content.filename, "report_"]
```

#### `endswith`
**功能**: 断言以指定字符串结尾  
**说明**: 检查实际值是否以期望值结尾

```yaml
validate:
  - endswith: [content.filename, ".json"]
  - endswith: [content.email, "@example.com"]
```

#### `regex_match`
**功能**: 断言正则表达式匹配  
**说明**: 检查实际值是否匹配期望的正则表达式

```yaml
validate:
  - regex_match: [content.phone, "^1[3-9]\\d{9}$"]
  - regex_match: [content.uuid, "^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$"]
```

### 6. 类型对比

#### `type_match`
**功能**: 断言类型匹配  
**说明**: 检查实际值的类型是否与期望类型匹配

```yaml
validate:
  - type_match: [content.count, int]
  - type_match: [content.price, float]
  - type_match: [content.name, str]
  - type_match: [content.active, bool]
  - type_match: [content.items, list]
  - type_match: [content.user, dict]
```

## 使用格式

HttpRunner 支持两种 validate 格式：

### 格式1（推荐）
```yaml
validate:
  - eq: [check_item, expected_value]
  - gt: [content.count, 0]
```

### 格式2（兼容旧版本）
```yaml
validate:
  - check: status_code
    comparator: eq
    expect: 200
  - check: content.message
    comparator: contains
    expect: "success"
```

## 实际应用示例

```yaml
- test:
    name: 用户信息接口验证
    request:
      url: /api/user/info
      method: GET
    validate:
      # 状态码验证
      - eq: [status_code, 200]
      
      # 响应结构验证
      - eq: [content.code, 0]
      - contains: [content.message, "成功"]
      
      # 数据类型验证
      - type_match: [content.data.user_id, int]
      - type_match: [content.data.username, str]
      - type_match: [content.data.is_active, bool]
      
      # 数值范围验证
      - gt: [content.data.user_id, 0]
      - ge: [content.data.age, 0]
      - le: [content.data.age, 150]
      
      # 字符串长度验证
      - len_gt: [content.data.username, 3]
      - len_le: [content.data.username, 50]
      
      # 字符串格式验证
      - regex_match: [content.data.email, "^[\\w\\.-]+@[\\w\\.-]+\\.[a-zA-Z]{2,}$"]
      - startswith: [content.data.avatar_url, "https://"]
      
      # 数组验证
      - type_match: [content.data.roles, list]
      - len_ge: [content.data.roles, 1]
      - contains: [content.data.permissions, "user:read"]
```

## 注意事项

1. **类型敏感**: 大部分对比项对数据类型敏感，建议使用 `str_eq` 进行字符串比较
2. **长度对比**: 长度相关的对比项适用于字符串、列表、字典等有长度概念的数据类型
3. **正则表达式**: 在 YAML 中使用正则表达式时注意转义字符
4. **变量引用**: 可以在期望值中使用变量引用，如 `$expected_code`
5. **函数调用**: 支持在检查项和期望值中使用函数调用

## 自定义对比项

**经源码确认**：HttpRunner 2.5.7 完全支持自定义对比项。如果内置对比项不满足需求，可以在 `debugtalk.py` 中自定义对比函数：

```python
# debugtalk.py
def custom_validator(check_value, expect_value):
    """自定义验证函数"""
    # 实现自定义验证逻辑
    assert check_value > expect_value * 2  # 示例：检查值是否大于期望值的2倍
    
def custom_range_check(check_value, expect_range):
    """自定义范围检查"""
    min_val, max_val = expect_range
    assert min_val <= check_value <= max_val
    
def custom_format_check(check_value, expect_pattern):
    """自定义格式检查"""
    import re
    assert re.match(expect_pattern, str(check_value))
```

在测试用例中使用（**推荐格式2**）：

```yaml
validate:
  # 自定义数值验证
  - check: content.score
    comparator: custom_validator
    expect: 50
    
  # 自定义范围验证  
  - check: content.age
    comparator: custom_range_check
    expect: [18, 65]
    
  # 自定义格式验证
  - check: content.phone
    comparator: custom_format_check
    expect: "^1[3-9]\\d{9}$"
```

**函数查找优先级**（源码确认）：
1. debugtalk.py 中的自定义函数
2. HttpRunner 内置函数
3. Python 内置函数

此文档涵盖了 HttpRunner 2.5.7 中所有可用的 validate 对比项，可以根据具体的测试需求选择合适的对比项进行验证。
