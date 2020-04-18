#choose the configuration
env = 

if env = dev or env = prd:
    import inky
    screen width = 202
    screen height = 104
elif env = dev:
    screen width = 202
    screen height = 104
    pass