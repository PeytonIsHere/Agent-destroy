def on_on_died():
    agent.teleport_to_player()
player.on_died(on_on_died)

def on_item_interacted_stone_sword():
    agent.turn(RIGHT_TURN)
player.on_item_interacted(STONE_SWORD, on_item_interacted_stone_sword)

def on_item_interacted_stone_pickaxe():
    for index in range(30):
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
player.on_item_interacted(STONE_PICKAXE, on_item_interacted_stone_pickaxe)

def on_on_chat():
    for index2 in range(30):
        agent.destroy(DOWN)
        agent.destroy(FORWARD)
        agent.move(DOWN, 1)
        agent.destroy(FORWARD)
        agent.move(FORWARD, 1)
        agent.collect_all()
player.on_chat(".", on_on_chat)

def on_item_interacted_wooden_hoe():
    agent.teleport_to_player()
    agent.drop_all(FORWARD)
player.on_item_interacted(WOODEN_HOE, on_item_interacted_wooden_hoe)

def on_on_chat2():
    player.tell(mobs.target(LOCAL_PLAYER), "\"STICK\"-TP agent")
    player.tell(mobs.target(LOCAL_PLAYER), "\"WOOD_HOE\"-Agent Drop all")
    player.tell(mobs.target(LOCAL_PLAYER),
        "\"STONE_SWORD\"-Agent turn right")
    player.tell(mobs.target(LOCAL_PLAYER), "\"STONE_PICK\"-Agent 3x3 tunnel")
    player.tell(mobs.target(LOCAL_PLAYER), "\"WOOD_PICK\"-Agent 3x3 hole")
    player.tell(mobs.target(LOCAL_PLAYER), "\"WOOD_SHOVEL\"-Agent bridge")
player.on_chat("Help", on_on_chat2)

def on_item_interacted_wooden_shovel():
    for index3 in range(30):
        agent.set_slot(1)
        if agent.detect(AgentDetection.BLOCK, FORWARD):
            agent.destroy(FORWARD)
        if agent.detect(AgentDetection.BLOCK, UP):
            agent.destroy(UP)
        if agent.detect(AgentDetection.BLOCK, DOWN):
            agent.collect_all()
        else:
            agent.place(DOWN)
        agent.move(FORWARD, 1)
player.on_item_interacted(WOODEN_SHOVEL, on_item_interacted_wooden_shovel)

def on_item_interacted_stick():
    agent.teleport(player.position(), player.get_orientation())
player.on_item_interacted(STICK, on_item_interacted_stick)

def on_item_interacted_wooden_pickaxe():
    for index4 in range(30):
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
player.on_item_interacted(WOODEN_PICKAXE, on_item_interacted_wooden_pickaxe)

player.tell(mobs.target(LOCAL_PLAYER),
    "Use these items no chat. say \"Help\"")
player.tell(mobs.target(LOCAL_PLAYER), "\"STICK\"-TP agent")
player.tell(mobs.target(LOCAL_PLAYER), "\"WOOD_HOE\"-Agent Drop all")
player.tell(mobs.target(LOCAL_PLAYER),
    "\"STONE_SWORD\"-Agent turn right")
player.tell(mobs.target(LOCAL_PLAYER), "\"STONE_PICK\"-Agent 3x3 tunnel")
player.tell(mobs.target(LOCAL_PLAYER), "\"WOOD_PICK\"-Agent 3x3 hole")
player.tell(mobs.target(LOCAL_PLAYER), "\"WOOD_SHOVEL\"-Agent bridge")
