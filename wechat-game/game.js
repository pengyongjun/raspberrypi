var myCanvas = wx.createCanvas()

var context = myCanvas.getContext('2d')
context.fillStyle = 'white'
context.fillRect(0, 0, 667, 375)

var image = wx.createImage()
image.onload = function () {
  console.log(image.width, image.height)
  context.drawImage(image, 0, 100)
}
image.src = 'res/rasp-logo.png'