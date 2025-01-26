s = """
01.课程简介
03:05
02.概述-Spring是什么
03:36
03.概述-Spring狭义和广义划分
03:14
04.概述-SpringFramework特点
02:29
05.概述-Spring模块组成和版本要求
02:05
06.入门-入门案例实现步骤
03:59
07.入门-入门案例程序开发
13:17
08.入门-入门案例程序分析
12:20
09.入门-整合Log4j2日志框架（上）
04:12
10.入门-整合Log4j2日志框架（下）
08:59
11.容器：IoC-概述（上）
06:42
12.容器：IoC-概述（中）
08:18
13.容器：IoC-概述（下）
06:27
14.容器：IoC-基于XML管理Bean-环境搭建
04:12
15.容器：IoC-基于XML管理Bean-获取Bean（上）
10:00
16.容器：IoC-基于XML管理Bean-获取Bean（中）
03:57
17.容器：IoC-基于XML管理Bean-获取Bean（下）
10:11
18.容器：IoC-基于XML管理Bean-依赖注入-setter注入（上）
05:29
19.容器：IoC-基于XML管理Bean-依赖注入-setter注入（下）
07:00
20.容器：IoC-基于XML管理Bean-依赖注入-构造器注入
06:29
21.容器：IoC-基于XML管理Bean-依赖注入-特殊值处理
06:58
22.容器：IoC-基于XML管理Bean-依赖注入-特殊类型属性-准备
08:20
23.容器：IoC-基于XML管理Bean-依赖注入-对象类型属性（上）
12:35
24.容器：IoC-基于XML管理Bean-依赖注入-对象类型属性（中）
05:18
25.容器：IoC-基于XML管理Bean-依赖注入-对象类型属性（下）
05:08
26.容器：IoC-基于XML管理Bean-依赖注入-数组类型属性
05:31
27.容器：IoC-基于XML管理Bean-依赖注入-List类型属性
07:01
28.容器：IoC-基于XML管理Bean-依赖注入-Map类型属性
13:21
29.容器：IoC-基于XML管理Bean-依赖注入-引入集合bean
15:16
30.容器：IoC-基于XML管理Bean-依赖注入-p命名空间
03:40
31.容器：IoC-基于XML管理Bean-引入外部属性文件
13:31
32.容器：IoC-基于XML管理Bean-Bean作用域
06:48
33.容器：IoC-基于XML管理Bean-bean生命周期（上）
14:47
34.容器：IoC-基于XML管理Bean-bean生命周期（下）
04:49
35.容器：IoC-基于XML管理Bean-FactoryBean
05:01
36.容器：IoC-基于XML管理Bean-自动装配（准备）
06:20
37.容器：IoC-基于XML管理Bean-自动装配（实现）
11:14
38.容器：IoC-基于注解管理Bean-创建Bean对象
18:17
39.容器：IoC-基于注解管理Bean-@Autowired注入（上）
11:51
40.容器：IoC-基于注解管理Bean-@Autowired注入（中）
06:34
41.容器：IoC-基于注解管理Bean-@Autowired注入（下）
09:45
42.容器：IoC-基于注解管理Bean-@Resource注入
14:32
43.容器：IoC-基于注解管理Bean-全注解开发
04:29
44.原理：手写IoC-回顾Java反射（上）
12:31
45.原理：手写IoC-回顾Java反射（中）
11:42
46.原理：手写IoC-回顾Java反射（下）
16:07
47.原理：手写IoC-实现步骤分析
07:15
48.原理：手写IoC-实现Bean创建（上）
10:22
49.原理：手写IoC-实现Bean创建（中）
23:11
50.原理：手写IoC-实现Bean创建（下）
24:26
51.原理：手写IoC-实现属性注入
12:46
52.面向切面：AOP-场景模拟
10:53
53.面向切面：AOP-代理模式（静态代理）
09:14
54.面向切面：AOP-代理模式（动态代理）
20:28
55.面向切面：AOP-AOP概念和术语
06:50
56.面向切面：AOP-基于注解的AOP-步骤分析
09:56
57.面向切面：AOP-基于注解的AOP-前置通知
20:44
58.面向切面：AOP-基于注解的AOP-各种通知
20:36
59.面向切面：AOP-基于注解的AOP-重用切入点和切面优先级
04:45
60.面向切面：AOP-基于XML的AOP-五种通知类型
11:43
61.单元测试：JUnit-Spring整合JUnit5和JUnit4
12:31
62.事务-JdbcTemplate-概述和准备
12:34
63.事务-JdbcTemplate-实现CRUD操作（上）
11:42
64.事务-JdbcTemplate-实现CRUD操作（下）
16:05
65.事务-基于注解的声明式事务-搭建案例环境
14:18
66.事务-基于注解的声明式事务-案例功能实现
14:02
67.事务-基于注解的声明式事务-案例添加事务
07:12
68.事务-基于注解的声明式事务-事务相关属性（上）
15:48
69.事务-基于注解的声明式事务-事务相关属性（下）
14:43
70.事务-基于注解的声明式事务-全注解配置事务
09:15
71.事务-基于XML的声明式事务-具体实现
20:05
72.资源操作：Resources-Resource接口和实现类（上）
18:52
73.资源操作：Resources-Resource接口和实现类（下）
05:11
74.资源操作：Resources-ResourceLoader接口
08:58
75.资源操作：Resources-ResourceLoaderAware接口
06:10
76.资源操作：Resources-使用Resource作为属性
07:17
77.资源操作：Resources-指定访问策略
07:39
78.国际化：i18n-Java国际化
10:38
79.国际化：i18n-Spring国际化
10:17
80.数据校验：Validation-通过Validator接口实现
17:39
81.数据校验：Validation-bean Validation注解实现
18:02
82.数据校验：Validation-基于方法实现校验
07:19
83.数据校验：Validation-自定义校验
09:36
84.提前编译：AOT-AOT概述
12:06
85.提前编译：AOT-Native Image构建（安装GraalVM编辑器）
09:19
86.提前编译：AOT-Native Image构建（安装C++编译环境）
04:49
87.提前编译：AOT-Native Image构建（实现构建）
07:19
88.课程总结
"""


def f(s):
    lines = s.split("\n")
    time_str = []
    for line in lines:
        if ":" in line:
            time_str.append(line)
    times = []
    for t in time_str:
        arr = t.split(":")
        if len(arr) == 2:
            minutes, seconds = t.split(":")
            times.append(int(minutes) + int(seconds) / 60)
        else:
            hours, minutes, seconds = t.split(":")
            times.append(int(hours) * 60 + int(minutes) + int(seconds) / 60)
    episode = input("Enter the episode you are on: ")
    print(sum(times[: int(episode)]) / 60)


f(s)
