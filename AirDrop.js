var succTrans = new Array();
var failTrans = new Array();

var closedDeal = new Array();
var redoDeal = new Array();

var unknownDeal = new Array();

function doTransfer(contOwner, ownerPwd) {
    //var nonce_ = 1001;
    //var macc = eth.accounts[0];
    web3.personal.unlockAccount(contOwner, ownerPwd);

    var lastpos = 0, batchLen = 100;
    var execBatch = function() {
        console.log('lastpos:' + lastpos);
        var batch = bills.slice(lastpos, lastpos + batchLen);
        //console.log(batch);
        web3.personal.unlockAccount(contOwner, ownerPwd);
        batch.forEach(function (bill) {
            var addr = bill.addr;
            var bal = bill.bal;
            var idx = bill.idx;
            try {
                var txHash = contInst.transfer(addr, web3.toWei(bal, 'ether'), {from: macc}); //, gasPrice: 20000000000});
                var trx = eth.getTransaction(txHash);
                msg = "[" + idx + ":] " + txHash + " {from: " + addr + ", val: " + bal + ", nonce: " + trx.nonce + "}";
                succTrans.push(msg);
                console.log(msg);
            } catch (e) {
                console.log(e);
                var msg = "{idx: " + idx + ", from: " + addr + ", val: " + bal + "}";
                failTrans.push(msg);
            }
        });
        if (lastpos + batchLen < bills.length) {
            setTimeout(execBatch, 2000);
            lastpos += batchLen;
        }
    }
    this.execBatch = execBatch;
}

function showTransResults() {
    succTrans.forEach(function (trans) {
       var trxInfo = trans.split(" ");
       var trxHash = trxInfo[1].split(":")[0];
       var trxObj = eth.getTransaction(trxHash);
       var trxBlockHash = trxObj.blockHash;

       if (trxBlockHash.substr(2, 10) != "0000000000") {
           var trxReceipt = eth.getTransactionReceipt(trxHash);
           var trxStatus = trxReceipt.status;
           if (trxStatus == "0x1") {
               trxInfo += " | [Block Hash:] " + trxBlockHash;
               closedDeal.push(trxInfo);
               console.log(trxInfo);
           }
           else if (trxStatus == "0x0") {
               redoDeal.push(trxInfo);
           } else {
               unknownDeal.push(trxInfo);
           }
       }
    });
}
