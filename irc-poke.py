import socket
from time import sleep

toNick = "nickname ..."             # your nickname (destinatary)


def IRCConnect(toNick, fromNick, ircMsg, network, port, ircDelay):
    carryon = True
    IRCsocket = None

    try:
        IRCsocket = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )

    except socket.error, msg:
        print msg
        carryon = False

    if carryon == True:
        try:
            IRCsocket.connect ((network, port))

        except socket.error, msg:
            IRCsocket.close()
            IRCsocket = None
            carryon = False
            print(msg)

    if carryon == True:
        try:
            trash = IRCsocket.recv (4096)

            IRCsocket.send ( 'NICK %s\r\n'%fromNick )
            IRCsocket.send ( 'USER %s 0 * :Blender Notifier\r\n'%fromNick )
            IRCsocket.send ( 'PRIVMSG %s : %s.\r\n'%(toNick, ircMsg) )
            IRCsocket.send ( 'QUIT %s\r\n' )
            trash = IRCsocket.recv (4096)
            sleep(ircDelay) #to give enough time to complete the conexion

            IRCsocket.close()

        except socket.error, (errno, msg):
            print("IRC Exception %s %s while receiving "%(errno,msg))
            carryon=False

        else:
            print ("IRC message sent:")
            print ("["+ircMsg+"]")


def main():

    network = 'irc.freenode.net'    # irc network address
    port = 6667                     # irc port (usually 6667)

    fromNick = "RedButton"  # don't need to change - ths user that will send the message

    ircMsg = "testing the button"    # message, frame number automatically added in the end
    ircDelay =  1                   # (5-10) pause in seconds to send the message

    IRCConnect(toNick, fromNick, ircMsg, network, port, ircDelay)


main()
