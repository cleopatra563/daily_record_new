lag() lead() 平替自连接 可以避免自连接带来的性能问题
跨行比较高效工具


写SQL时注意：
1、表和字段，互相关系
2、写意义的注释，有意义的列名称，有意义的表别名

核心概念&方法论
1、什么是有序数据、状态流转、操作路径
连续登录天数、计算事件间间隔、检测特定模式（事件A->事件B->事件C）
分组排序和排名
生产 质检 出库
login->建筑升级->人物增强->玩家战斗->下线退出


核心原理&执行原理&底层原理
group by 分组排序和排名->分配行号

实战作业
1、表结构设计
2、场景分析
3、sql实现
4、输出结果

最佳实践与避坑指南

/*连续天数中*/
login_date - row_number() over(partition by order by "#event_time")
with login_group(
 select role_id,login_date,login_date - row_number() over(partition by role_id order by time) as grp 输出行号辅助列
 from daily_login
),
 consecutive_logins(
select role_id,grp,
count(*) as consecutive_days
min(login_date) as start_date
max(login_date)
from login_group
group by role_id,grp
having count(*)>=3  --连续登录3天以上
 )
select role_id,start_date,end_date,consecutive_days
from consecutive_logins
order by role_id,start_date;

 role1 2023-12-20-2 2023-12-18
 role1 2023-12-19-1 2023-12-18
 role1 2023-12-21-3 2023-12-18
