def on_on_died():
    agent.teleport_to_player()
player.on_died(on_on_died)

def on_item_interacted_stone_sword():
    agent.turn(RIGHT_TURN)
player.on_item_interacted(STONE_SWORD, on_item_interacted_stone_sword)

def on_on_chat():
    for index in range(40):
        agent.destroy(FORWARD)
        agent.move(FORWARD, 1)
        agent.destroy(UP)
        agent.collect_all()
player.on_chat("..", on_on_chat)

def on_item_interacted_wooden_sword():
    for index2 in range(40):
        agent.destroy(DOWN)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(FORWARD)
        agent.destroy(BACK)
        agent.move(FORWARD, 1)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.move(BACK, 2)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.move(FORWARD, 1)
        agent.move(DOWN, 1)
        agent.collect_all()
player.on_item_interacted(WOODEN_SWORD, on_item_interacted_wooden_sword)

def on_item_interacted_stone_pickaxe():
    for index3 in range(40):
        agent.destroy(FORWARD)
        agent.move(FORWARD, 1)
        agent.destroy(UP)
        agent.collect_all()
player.on_item_interacted(STONE_PICKAXE, on_item_interacted_stone_pickaxe)

def on_on_chat2():
    for index4 in range(30):
        agent.destroy(DOWN)
        agent.destroy(FORWARD)
        agent.move(DOWN, 1)
        agent.destroy(FORWARD)
        agent.move(FORWARD, 1)
        agent.collect_all()
player.on_chat(".", on_on_chat2)

def on_item_interacted_stick():
    agent.teleport(player.position(), player.get_orientation())
player.on_item_interacted(STICK, on_item_interacted_stick)

def on_item_interacted_wooden_pickaxe():
    for index5 in range(40):
        agent.destroy(FORWARD)
        agent.destroy(UP)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(DOWN)
        agent.move(UP, 1)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.move(DOWN, 2)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.move(UP, 1)
        agent.move(FORWARD, 1)
        agent.collect_all()
player.on_item_interacted(WOODEN_PICKAXE, on_item_interacted_wooden_pickaxe)
