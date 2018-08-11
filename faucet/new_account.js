let Eos = require('eosjs');
let fs = require('fs');

let httpEndpoint = 'https://eost.travelchain.io';
let chainId = '0443d062bb782b32bdc07a65273e1696c9a28749c047124927c7160897cacd28';

let creator = process.env.REGISTRATOR_NAME;


let newaccount = process.argv[2];
let owner_key = process.argv[3];
let active_key = process.argv[4];

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
    bytes: 4000
  })
  tr.delegatebw({
    from: creator,
    receiver: newaccount,
    stake_net_quantity: '10.0000 TT',
    stake_cpu_quantity: '10.0000 TT',
    transfer: 1
  })
})
.then((data) => {
  console.log(JSON.stringify(data));

}).catch((e) => {
    // error in JSON
    console.log(e);
  });
