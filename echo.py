from rill_framework import Autotest
import sys


# 项目名称，和测试用例、页面元素表文件名称中的项目名称必须一致
# 此处项目名称更准确的表述应该是：测试计划名称。
plan_name = 'Echo'

# 单 sheet 页面模式
sheet_name = 'echo'

# sheet 页面匹配模式，仅支持结尾带*
#sheet_name = 'TestCase*'

# sheet 页面列表模式
#sheet_name = ['TestCase', 'test']

# 环境配置信息
# Http api
desired_caps = {'platformName': 'api'}
server_url = ''


# 初始化自动化实例
rill = Autotest(plan_name, sheet_name, desired_caps, server_url)

# 按条件执行,支持筛选的属性有：'id', 'title', 'designer', 'priority'
# rill.fliter(priority='H')

# 执行自动化测试
rill.plan()


# 如果是集成到 CI/CD，则给出退出码；也可以根据上面的测试结果自己生成退出码
#sys.exit(rill.code)
 