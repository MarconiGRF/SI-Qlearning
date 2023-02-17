import socket


def connect(port):
    """
    Connects to the game port to be able to send input commands.

    :param port: The port that the game is running in localhost.
    :return: A socket to control the game.
    """
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect(('127.0.0.1', port))
        print('[CONNECTION] OK.')
        return s
    except:
        print('[CONNECTION] Failed to connect to the port.')
        return 0

    else:
        print('[CONNECTION] Continuing...')


#Da o estado e a recompensa que o agente recebeu
def get_state_reward(s , act):
    """
    Given the input returns the state and the reward associated to it.
    Sends data to the game, reads it back and converts to meaningful data to QLearning algorithm.

    :param s: The state
    :param act: The action performed
    :return: A tuple containing state and reward.
    """
    s.send(str(act).encode())
    data = "" 
    data_recv = False;
    while(not data_recv):
        data = s.recv(1024).decode()
        try:
            data = eval(data)
            data_recv = True
        except:
            data_recv = False

    # Convert the data to decimal int
    state = data['estado']
    state = state[2:]

    reward = data['recompensa']

    return state, reward
