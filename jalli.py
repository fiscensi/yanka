const TelegramBot = require('node-telegram-bot-api')

const token = '673228744:AAGBW1TaknLHbnF2NH2sBXnIlkk7n_7cSJQ'

const bot = new TelegramBot(token, {polling: true})


bot.on('message', msg => {
  bot.sendMessage(msg.chat.id, `Hello world, bot says: "Hi, ${msg.from.first_name}"`)
})
