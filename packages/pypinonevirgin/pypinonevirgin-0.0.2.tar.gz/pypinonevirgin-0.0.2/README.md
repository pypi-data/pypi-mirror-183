# pypi
Build My first PyPI package
PyPI : the Python Package Index

###### tags: `Python` `PyPI`

## Steps-by-Steps
1. 準備好要上傳 PyPI 的套件
    > :memo: 
    > 1. 資料夾結構
    > ![steps_0.png](https://i.imgur.com/fUDgUGv.png)


2. 進入該層目錄 : `cd C:\Users\chichun.chen\Desktop\git\pypi`

3. 打包檢查 : `python setup.py check`

4. 打包 : `python setup.py sdist`
    > :memo: 
    > 1. **sdist** : 較常用，支持 **pip** 安裝
    > 2. bdist_egg : 支持 easy_install 安装
    > 3. 打包好的檔案會在 `/dist` 底下
    > ![steps_1.png](https://i.imgur.com/InQ2tEs.png)
    > 
    > 4. 使用 `pip install pypinonevirgin-0.0.1.tar.gz` 測試打包完的檔案是否能正確執行

5. 安裝 **twine** 作為後續上傳 PyPI 用 : `pip install twine`

6. 註冊 [PyPI](https://pypi.org/)

7. 上傳 : `twine upload dist/*`
    > :memo: 
    > 1. 需註冊 PyPI 帳號密碼
    > ![steps_2.png](https://i.imgur.com/xSqHkps.png)

## FAQ
* Register Fail:
    * **Command** : `python setup.py register`
    * **ErrorMsg** : Server response (410): Project pre-registration is no longer required or supported, upload your files instead.
    * **Explain** : PyPI 因為 HTTP 安全性認證的問題，不再支援 register、upload 等指令
    * **Solution** : 改用 `twine upload` (官方建議)

* Upload Fail : 
    * **Command** : `twine upload dist/*`
    * **ErrorMsg** : HTTPError: 400 Bad Request: This filename has already been used, use a different version.
    * **Explain** : PyPI 上已經存在相同名稱的套件/版號
    * **Solution** : 更改套件名稱 or 調整版號

* console_scripts : 
    > :memo: 
    > 1. Build python scripts automatically
    > ![steps_3.png](https://i.imgur.com/hICMmdU.png)



## Windows 打印資料夾結構的小工具
```powershell=
tree <yourPath> /f | Select-Object -Skip 2 | ForEach-Object {
	if ($_.Contains(':\')) {
		Write-Host $_ -ForegroundColor Cyan
	}
	elseif ($_.Contains('─')) {
		Write-Host "$($_.Replace('─', '─<'))>" -ForegroundColor Yellow
	}
	else{
		Write-Host $_ -ForegroundColor White
	}
}

```

## Reference
* [PyPI Official](https://pypi.org/)
* [PyPI 教學](https://zhuanlan.zhihu.com/p/26159930)
* [PyPI 教學](https://www.cnblogs.com/jaysonteng/p/15221886.html)
* [輸出資料夾結構](https://blog.darkthread.net/blog/dump-folder-tree/)