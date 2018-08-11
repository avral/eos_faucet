let Eos = require('eosjs');
let fs = require('fs');

let httpEndpoint = process.env.EOS_NODE_URL;
let chainId = process.env.EOS_NODE_CHAIN_ID;
let creator = process.env.REGISTRATOR_NAME;


let newaccount = process.argv[2];
let owner_key = process.argv[3];
let active_key = process.argv[4];

// FOR TEST
//let newaccount = 'lololol.tc';
//let owner_key = 'EOS7YHYVETD44VTFdjYCBtpVuiNfdZmSqqnGGKwgKPqvoBaHfuNxk';
//let active_key = 'EOS7YHYVETD44VTFdjYCBtpVuiNfdZmSqqnGGKwgKPqvoBaHfuNxk';

let keyProvider = [process.env.REGISTRATOR_WIF];

eos = Eos({httpEndpoint, chainId, keyProvider, logger: {error: null}});

eos.transaction(tr => {
  tr.newaccount({
    creator: creator,
    name: newaccount,
    owner: owner_key,
    active: active_key
  })
  tr.buyrambytes({
    payer: creator,
    receiver: newaccount,
    bytes: 8192
  })
  tr.delegatebw({
    from: creator,
    receiver: newaccount,
    stake_net_quantity: '1.0000 TT',
    stake_cpu_quantity: '1.0000 TT',
    transfer: 1
  })
})
.then((data) => {
  console.log(JSON.stringify(data));

}).catch((e) => {
    // error in JSON
    console.log(e);
  });
