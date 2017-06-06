// var timeString = function(timestamp) {
//     t = new Date(timestamp * 1000)
//     t = t.toLocaleTimeString()
//     return t
// }
//
// var weiboTemplate = function(weibo) {
//     var title = weibo.title
//     var content = weibo.content
//     var id = weibo.id
//     var ct = timeString(weibo.created_time)
//     var t = `
//         <div class="weibo-cell" id='weibo-${id}' data-id="${id}">
//             <div class="weibo-username">{{w.user().username}}</div>
//             <a>
//                 <img class=weibo-head-img src={{ '/uploads/' + w.user().user_image + '?v=3&amp;s=120' }}title="atian25"/>
//             </a>
//             <span class='weibo-title'>${title}</span>
//             <span class='weibo-content'>${content}</span>
//             <time class='weibo-ut'>${ct}</time>
//             <button class="weibo-delete">删除</button>
//         </div>
//     `
//     return t
//
// }
//
// var insertweibo = function(weibo) {
//     var weiboCell = weiboTemplate(weibo)
//     // 插入 weibo-list
//     var weiboList = e('.weibo-list')
//     weiboList.insertAdjacentHTML('beforeend', weiboCell)
// }
//
// var insertEditForm = function(cell) {
//     var form = `
//         <div class='weibo-edit-form'>
//             <input class="weibo-edit-input">
//             <button class='weibo-update'>更新</button>
//         </div>
//     `
//     cell.insertAdjacentHTML('beforeend', form)
// }
//
// var loadweibos = function() {
//     // 调用 ajax api 来载入数据
//     apiweiboAll(function(r) {
//         // console.log('load all', r)
//         // 解析为 数组
//         var weibos = JSON.parse(r)
//         // 循环添加到页面中
//         for(var i = 0; i < weibos.length; i++) {
//             var weibo = weibos[i]
//             insertweibo(weibo)
//         }
//     })
// }
//
// var bindEvents = function() {
//
// }
//
// var __main = function() {
//     loadweibos()
// }
//
// __main()
