# docker-django-demo

#### 介绍

| tag | 说明 |
| --- | --- |
| v1.0.0-20240729 | 使用docker做开发环境 |
| v1.1.0-20240729 | 使用IDE连接docker做开发 |
| v1.2.0-20240729 | 多个django服务 |
| v1.3.0-20240729 | nginx负载均衡 |


TODO:
- 使用docker做开发环境
- 使用IDE连接docker做开发
- 多个django服务
- nginx负载均衡
  - 负载均衡的验证 环境变量法
- 数据的保存恢复
- cicd
    - CI/CD执行很慢, 有时候image没有改变, 不需要build image, 使用原来的image即可, 应该怎么编写 yaml. 比较复杂
    - 生成image, 并且使用latest. TODO: 查看别人的 build  push 逻辑
- ab测试

<!-- 600MB
多阶段构建!!
120MB -->

mysql 400M
postgres 20M
