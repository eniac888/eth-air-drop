该项目包括：
1. BAI合约升级为2.0版本。
2. 从链上抓取旧合约token holders以及transfer等相关数据的脚本(目前从etherscan爬取，由于etherscan有CloudFlare，会禁止爬虫，未来还需研究其他途径的链上合约相关数据获取方式)。
3. 为所有token holders更换合约所需批量空投token的web3脚本，通过geth console运行。

空投脚本执行方式：
1. 准备工作。token holders已以列表形式保存在holders.txt文件中. 运行ConvertBills.py, holders.txt中的数据将会以JSON数组的形式存入名为bill.js的文件,打开该文件，在文件内容最前面加上
   bills = 
2. 按需要修改build.sh中合约源代码文件和编译的目标文件, 目前该目录中BAI2.0合约的源代码文件为coin.sol, 目标文件为coin.js. 若.js文件不存在，则执行build.sh进行编译.
3. 进入geth控制台。在geth已运行的机器上，通过geth attach进入控制台，若geth未运行，则通过geth [options] console运行, 在geth控制台中执行:
       macc = eth.accounts[0]
   以方便后续调用，该用法仅适用于合约的创建者为该节点上的etherbase的情况。后续所有命令均在控制台中执行.
4. loadScript("./coin.js"). 加载编译好的合约目标文件. 加载成功后，输入baiCoin回车，可以看到编译好后的合约的ABI及Byte Code.
5. abi = baiCoin.contracts["coin.sol:BAI20"].abi. 获取合约的ABI code;
6. BaiContract = eth.contract(JSON.parse(abi));
7. contInst = BaiContract.at("<合约地址>"); 注：合约实例名必须与AirDrop里所用实例名一样，目前脚本里就叫contInst. 合约实例创建成功后，可通过contInst.totalSupply, contInst.balanceOf("<钱包地址>"), contInst.name() 等查看相关数据等确认合约是否创建成功.
8. loadScript("./bills.js"). 确认脚本加载成功(加载成功后，输入bills回车，可以看到所有token holders的JSON数据)
9. loadScript("./AirDrop.js"). 加载成功后便有了名为function doTransfer(contOwner, ownerPwd)的函数定义
10. new doTransfer(macc, "q1w2e3r4t5").execBatch(). 按需要修改密码。
