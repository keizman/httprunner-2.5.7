
# HttpRunner

[![downloads](https://pepy.tech/badge/httprunner)](https://pepy.tech/project/httprunner)
[![unittest](https://github.com/httprunner/httprunner/workflows/unittest/badge.svg
)](https://github.com/httprunner/httprunner/actions)
[![integration-test](https://github.com/httprunner/httprunner/workflows/integration_test/badge.svg
)](https://github.com/httprunner/httprunner/actions)
[![codecov](https://codecov.io/gh/httprunner/httprunner/branch/master/graph/badge.svg)](https://codecov.io/gh/httprunner/httprunner)
[![pypi version](https://img.shields.io/pypi/v/httprunner.svg)](https://pypi.python.org/pypi/httprunner)
[![pyversions](https://img.shields.io/pypi/pyversions/httprunner.svg)](https://pypi.python.org/pypi/httprunner)
[![TesterHome](https://img.shields.io/badge/TTF-TesterHome-2955C5.svg)](https://testerhome.com/github_statistics)

*HttpRunner* is a simple & elegant, yet powerful HTTP(S) testing framework. Enjoy! ✨ 🚀 ✨


prompt:
```
请在源码中添加 variables_af , block 作用时间再 extract 之后, 解决 设置 变量失败问题.
注意: 
variables_af 中调用 update_test_variables 时，可能需要确保 test_variables_mapping 是最新的。
variables_af 的实现，确保变量也被添加到 session_variables_mapping 中：

function_regex_compile = re.compile(r"\$\{(\w+)\(([\$\w\s,\"'\[\]]*)\)\}")
parser.py
主要变化：
•  添加了 \[ 和 \] 支持方括号
•  移除了 \. 和 \-/= 一些不必要的字符，简化为核心需要的字符
```

2025-08-25 添加 variables_af 功能，支持在 extract 之后执行变量赋值
- 新增 `variables_af` 配置项，在 extract 之后、validate 之前执行
- 解决了 variables 在 extract 之前执行导致无法使用提取的数据的问题
- 支持对提取的数据进行函数处理并设置新变量
- 设置的变量可以通过 output 导出给后续测试步骤使用

使用示例：
```yaml
teststeps:
- name: 测试步骤
  api: api/test.yml
  extract:
    media_url: content.url
  variables_af:  # 在 extract 之后执行
    processed_url: ${process_url($media_url)}
  output:
    - processed_url
```




2025-08-22 添加针对于 testcase 级别的 rerun 机制, 减少环境干扰造成的用例执行失败
- 使用示例 --rerun 1 代表在这个 testcase 失败后重新跑一次这个 testcase 文件. 
- 测试报告添加 rerun 次数 1/1 
- 更换 defualt 测试报告文件为 extent_report_template_httprunner2
- 添加用例统计饼状图上的成功/失败比例的统计信息



