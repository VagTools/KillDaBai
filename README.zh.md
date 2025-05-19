# KillDaBai

## 软件开发背景

在部分电脑上，使用过“大白映射”工具的 Softether 映射功能后，其他软件的 Softether 功能会出现异常。这是因为大白的 Softether 会修改默认的 Windows 服务路径，并使用其自带的便携式 Softether 版本，导致其他软件的 Softether 无法正常工作，即使重新安装也无法恢复。

本工具旨在解决此问题。它会自动：
- 停止大白 Softether 相关的 Windows 服务
- 删除这些服务
- 删除大白映射释放的 Softether 目录

完成上述操作后，您可以重新安装 Softether，或让其他软件自带的 Softether 恢复正常使用。

## 下载地址

您可以在这里下载最新版：
[https://github.com/VagTools/KillDaBai/releases](https://github.com/VagTools/KillDaBai/releases)

## 使用方法

1. 右键以“管理员身份运行” KillDaBai.exe。
2. 程序会自动停止并删除相关服务和目录。
3. 操作完成后，您可以重新安装或使用其他软件自带的 Softether。

> 注意：必须以管理员权限运行，否则操作会失败。

---

如有疑问，请联系开发者。
