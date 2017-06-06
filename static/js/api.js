// var log = function() {
//   console.log.apply(console, arguments);
// }
//
// var e = function(sel) {
//   return document.querySelector(sel)
// }
//
// var ajax = function(method, path, data, responseCallback) {
//     var r = new XMLHttpRequest()
//     r.open(method, path, true)
//     r.setRequestHeader('Content-Type', 'application/json')
//     r.onreadystatechange = function() {
//         if(r.readyState === 4) {
//             responseCallback(r.response)
//         }
//     }
//     data = JSON.stringify(data)
//     r.send(data)
// }
//
// // Weibo API
// // 获取所有 weibo
// var apiWeiboAll = function(callback) {
//     var path = '/api/weibo/all'
//     ajax('GET', path, '', callback)
// }
