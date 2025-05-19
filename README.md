# KillDaBai

## Overview

On some computers, after using the "Dabai Mapping" tool's Softether mapping feature, other software's Softether functionality may stop working properly. This is because Dabai's Softether modifies the default Windows service path and uses its own portable Softether version, causing conflicts that prevent other software's Softether from functioning, even after reinstallation.

This tool is designed to solve this problem. It will automatically:
- Stop Dabai Softether-related Windows services
- Delete these services
- Remove the Softether directory released by Dabai Mapping

After these operations, you can reinstall Softether or use other software's built-in Softether normally.

[中文介绍](README.zh.md)

## Download

You can download the latest release here:
[https://github.com/VagTools/KillDaBai/releases](https://github.com/VagTools/KillDaBai/releases)

## Usage

1. Right-click and select "Run as administrator" for KillDaBai.exe.
2. The program will automatically stop and delete the related services and directories.
3. After completion, you can reinstall or use other software's Softether as needed.

> Note: You must run as administrator, otherwise the operations will fail.

---

If you have any questions, please contact the developer.

---



