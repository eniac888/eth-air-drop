var succTrans = new Array();
var failTrans = new Array();

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
                var txHash = contInst.transfer(addr, web3.toWei(bal, 'ether'), {from: macc});
                var trx = eth.getTransaction(txHash);
                msg = "[" + idx + ":] " + txHash + ": {from: " + addr + ", val: " + bal + ", nonce: " + trx.nonce + "}";
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
