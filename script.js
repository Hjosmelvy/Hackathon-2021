global.fetch = require("node-fetch");
//Prints number of followers based off of company twitter account name
let getNumberOfFollowers = async (userName) => {

    let response = await fetch('https://cdn.syndication.twimg.com/widgets/followbutton/info.json?screen_names=' + userName).then(res => res.json());
    return response;
    
  }

let name = (async () => {
  let data = await getNumberOfFollowers("basf");
  console.log(data);

})()
// name = JSON.parse(name);
