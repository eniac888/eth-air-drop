该项目包括：
1. BAI合约升级为2.0版本。
2. 从链上抓取旧合约token holders以及transfer等相关数据的脚本(目前从etherscan爬取，由于etherscan有CloudFlare，会禁止爬虫，未来还需研究其他途径的链上合约相关数据获取方式)。
3. 为所有token holders更换合约所需批量空投token的web3脚本，通过geth console运行。