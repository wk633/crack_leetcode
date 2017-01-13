// 实现命令行创建文件夹和文件
var fs = require('fs');
var argv = require('optimist').argv

var existWarning = function(name){
  console.log(name + ' already exists')
}
var createFile = function(dir,name){
  fs.writeFile(dir+'/'+name,"",(err) => {
    if(err) throw err;
    console.log(name + ' is created')
  })
}

if(argv.d){
  // need create folder
  var dirname = './'+argv.d
  if(fs.existsSync(dirname)){
    existWarning(dirname)
  }else{
    fs.mkdirSync(dirname)
  }

  if(argv.f){
    var filename1 = argv.f + '.md'
    var filename2 = argv.f + '.py'
    if(fs.existsSync(filename1)){
      existWarning(filename1)
    }else{
      createFile(dirname, filename1)
    }
    if(fs.existsSync(filename2)){
      existWarning(filename2)
    }else{
      createFile(dirname, filename2)
    }
  }
}else{
  console.log('please assign a dirname by --d=dirname')
}
