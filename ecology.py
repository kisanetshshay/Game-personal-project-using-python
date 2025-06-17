import random

HABITATS = ['Forest', 'Wetland', 'Grassland']

SPECIES_CARDS = [
    
    {"name": "Oak Tree", "type": "Producer", "habitat": "Forest", "eats": [], "eaten_by": ["Caterpillar"], "desc": "Provides food and shelter."},
    {"name": "Water Lily", "type": "Producer", "habitat": "Wetland", "eats": [], "eaten_by": ["Snail"], "desc": "Grows in ponds and wetlands."},
    {"name": "Grass", "type": "Producer", "habitat": "Grassland", "eats": [], "eaten_by": ["Rabbit"], "desc": "Common plant in grasslands."},
    {"name": "Maple Tree", "type": "Producer", "habitat": "Forest", "eats": [], "eaten_by": ["Deer"], "desc": "Maple trees produce seeds eaten by animals."},
    {"name": "Cattail", "type": "Producer", "habitat": "Wetland", "eats": [], "eaten_by": ["Muskrat"], "desc": "Provides shelter and food in wetlands."},
    {"name": "Wildflower", "type": "Producer", "habitat": "Grassland", "eats": [], "eaten_by": ["Bee"], "desc": "Attracts pollinators."},
    {"name": "Fern", "type": "Producer", "habitat": "Forest", "eats": [], "eaten_by": ["Slug"], "desc": "Shade-loving plant."},
    {"name": "Algae", "type": "Producer", "habitat": "Wetland", "eats": [], "eaten_by": ["Fish"], "desc": "Base of aquatic food chains."},
    {"name": "Shrub", "type": "Producer", "habitat": "Grassland", "eats": [], "eaten_by": ["Goat"], "desc": "Provides cover for small animals."},
    {"name": "Moss", "type": "Producer", "habitat": "Forest", "eats": [], "eaten_by": ["Slug"], "desc": "Retains moisture on forest floor."},
    {"name": "Duckweed", "type": "Producer", "habitat": "Wetland", "eats": [], "eaten_by": ["Duck"], "desc": "Floats on water surfaces."},
    {"name": "Sedge", "type": "Producer", "habitat": "Grassland", "eats": [], "eaten_by": ["Grasshopper"], "desc": "Grasslike plant."},
    {"name": "Pine Tree", "type": "Producer", "habitat": "Forest", "eats": [], "eaten_by": ["Squirrel"], "desc": "Produces cones rich in seeds."},
    {"name": "Reed", "type": "Producer", "habitat": "Wetland", "eats": [], "eaten_by": ["Beetle"], "desc": "Tall wetland grass."},
    {"name": "Clover", "type": "Producer", "habitat": "Grassland", "eats": [], "eaten_by": ["Rabbit"], "desc": "Fixes nitrogen in soil."},


    {"name": "Rabbit", "type": "Primary Consumer", "habitat": "Grassland", "eats": ["Grass", "Clover"], "eaten_by": ["Hawk", "Fox"], "desc": "Eats grass and clover."},
    {"name": "Caterpillar", "type": "Primary Consumer", "habitat": "Forest", "eats": ["Oak Tree", "Maple Tree"], "eaten_by": ["Bird"], "desc": "Eats leaves."},
    {"name": "Snail", "type": "Primary Consumer", "habitat": "Wetland", "eats": ["Water Lily"], "eaten_by": ["Duck"], "desc": "Feeds on aquatic plants."},
    {"name": "Deer", "type": "Primary Consumer", "habitat": "Forest", "eats": ["Maple Tree"], "eaten_by": ["Wolf"], "desc": "Browses on young trees."},
    {"name": "Grasshopper", "type": "Primary Consumer", "habitat": "Grassland", "eats": ["Sedge"], "eaten_by": ["Frog"], "desc": "Eats leaves and grass."},
    {"name": "Bee", "type": "Primary Consumer", "habitat": "Grassland", "eats": ["Wildflower"], "eaten_by": ["Bird"], "desc": "Pollinates flowers."},
    {"name": "Slug", "type": "Primary Consumer", "habitat": "Forest", "eats": ["Fern", "Moss"], "eaten_by": ["Toad"], "desc": "Eats soft plants."},
    {"name": "Fish", "type": "Primary Consumer", "habitat": "Wetland", "eats": ["Algae"], "eaten_by": ["Heron"], "desc": "Feeds at the bottom of ponds."},
    {"name": "Muskrat", "type": "Primary Consumer", "habitat": "Wetland", "eats": ["Cattail"], "eaten_by": ["Fox"], "desc": "Feeds in marshes."},
    {"name": "Goat", "type": "Primary Consumer", "habitat": "Grassland", "eats": ["Shrub"], "eaten_by": ["Wolf"], "desc": "Browses on shrubs."},
    {"name": "Squirrel", "type": "Primary Consumer", "habitat": "Forest", "eats": ["Pine Tree"], "eaten_by": ["Hawk"], "desc": "Eats seeds and nuts."},
    {"name": "Duck", "type": "Primary Consumer", "habitat": "Wetland", "eats": ["Duckweed"], "eaten_by": ["Fox"], "desc": "Feeds on floating plants."},
    {"name": "Beetle", "type": "Primary Consumer", "habitat": "Wetland", "eats": ["Reed"], "eaten_by": ["Frog"], "desc": "Eats plant material."},
    {"name": "Mouse", "type": "Primary Consumer", "habitat": "Grassland", "eats": ["Grass"], "eaten_by": ["Snake"], "desc": "Small rodent."},
    {"name": "Toad", "type": "Primary Consumer", "habitat": "Forest", "eats": ["Slug"], "eaten_by": ["Snake"], "desc": "Eats insects and slugs."},
    {"name": "Frog", "type": "Primary Consumer", "habitat": "Wetland", "eats": ["Grasshopper", "Beetle"], "eaten_by": ["Heron"], "desc": "Eats insects."},
    {"name": "Bird", "type": "Primary Consumer", "habitat": "Forest", "eats": ["Caterpillar", "Bee"], "eaten_by": ["Hawk"], "desc": "Eats insects and seeds."},
    {"name": "Heron", "type": "Primary Consumer", "habitat": "Wetland", "eats": ["Fish", "Frog"], "eaten_by": ["Fox"], "desc": "Wading bird."},
    {"name": "Ant", "type": "Primary Consumer", "habitat": "Forest", "eats": ["Moss"], "eaten_by": ["Bird"], "desc": "Eats small plants."},
    {"name": "Butterfly", "type": "Primary Consumer", "habitat": "Grassland", "eats": ["Wildflower"], "eaten_by": ["Bird"], "desc": "Pollinates flowers."},

    
    {"name": "Hawk", "type": "Secondary Consumer", "habitat": "Grassland", "eats": ["Rabbit", "Squirrel", "Bird"], "eaten_by": [], "desc": "Top predator."},
    {"name": "Fox", "type": "Secondary Consumer", "habitat": "Grassland", "eats": ["Rabbit", "Duck", "Heron", "Muskrat"], "eaten_by": [], "desc": "Omnivorous predator."},
    {"name": "Wolf", "type": "Secondary Consumer", "habitat": "Forest", "eats": ["Deer", "Goat"], "eaten_by": [], "desc": "Pack hunter."},
    {"name": "Snake", "type": "Secondary Consumer", "habitat": "Forest", "eats": ["Mouse", "Toad"], "eaten_by": ["Hawk"], "desc": "Slithering predator."},
    {"name": "Frog", "type": "Secondary Consumer", "habitat": "Wetland", "eats": ["Beetle", "Grasshopper"], "eaten_by": ["Heron"], "desc": "Also eats insects."},
    {"name": "Heron", "type": "Secondary Consumer", "habitat": "Wetland", "eats": ["Fish", "Frog"], "eaten_by": ["Fox"], "desc": "Eats small animals."},
    {"name": "Toad", "type": "Secondary Consumer", "habitat": "Forest", "eats": ["Slug"], "eaten_by": ["Snake"], "desc": "Eats insects and slugs."},
    {"name": "Lizard", "type": "Secondary Consumer", "habitat": "Grassland", "eats": ["Butterfly"], "eaten_by": ["Hawk"], "desc": "Eats insects."},
    {"name": "Owl", "type": "Secondary Consumer", "habitat": "Forest", "eats": ["Mouse"], "eaten_by": [], "desc": "Nocturnal bird of prey."},
    {"name": "Shrew", "type": "Secondary Consumer", "habitat": "Grassland", "eats": ["Ant"], "eaten_by": ["Owl"], "desc": "Small insectivore."},
    {"name": "Mantis", "type": "Secondary Consumer", "habitat": "Grassland", "eats": ["Grasshopper"], "eaten_by": ["Bird"], "desc": "Ambushes prey."},
    {"name": "Spider", "type": "Secondary Consumer", "habitat": "Forest", "eats": ["Butterfly"], "eaten_by": ["Bird"], "desc": "Spins webs."},
    {"name": "Badger", "type": "Secondary Consumer", "habitat": "Grassland", "eats": ["Rabbit"], "eaten_by": [], "desc": "Digs for prey."},
    {"name": "Weasel", "type": "Secondary Consumer", "habitat": "Forest", "eats": ["Squirrel"], "eaten_by": ["Hawk"], "desc": "Small quick predator."},
    {"name": "Bat", "type": "Secondary Consumer", "habitat": "Forest", "eats": ["Bee"], "eaten_by": ["Owl"], "desc": "Eats insects at night."},

    {"name": "Fungi", "type": "Decomposer", "habitat": "Forest", "eats": ["Dead Plant"], "eaten_by": [], "desc": "Breaks down dead matter."},
    {"name": "Earthworm", "type": "Decomposer", "habitat": "Grassland", "eats": ["Dead Plant"], "eaten_by": ["Bird"], "desc": "Improves soil."},
    {"name": "Bacteria", "type": "Decomposer", "habitat": "Wetland", "eats": ["Dead Plant"], "eaten_by": [], "desc": "Microscopic recycler."},
    {"name": "Mold", "type": "Decomposer", "habitat": "Forest", "eats": ["Dead Plant"], "eaten_by": [], "desc": "Grows on decaying matter."},
    {"name": "Millipede", "type": "Decomposer", "habitat": "Forest", "eats": ["Dead Plant"], "eaten_by": ["Bird"], "desc": "Feeds on detritus."},
    {"name": "Snail", "type": "Decomposer", "habitat": "Wetland", "eats": ["Dead Plant"], "eaten_by": ["Duck"], "desc": "Also eats dead material."},
    {"name": "Woodlouse", "type": "Decomposer", "habitat": "Forest", "eats": ["Dead Plant"], "eaten_by": ["Bird"], "desc": "Breaks down wood."},
    {"name": "Maggot", "type": "Decomposer", "habitat": "Grassland", "eats": ["Dead Animal"], "eaten_by": ["Bird"], "desc": "Eats dead animals."},
    {"name": "Nematode", "type": "Decomposer", "habitat": "Wetland", "eats": ["Dead Plant"], "eaten_by": [], "desc": "Tiny soil animal."},
    {"name": "Springtail", "type": "Decomposer", "habitat": "Grassland", "eats": ["Dead Plant"], "eaten_by": ["Bird"], "desc": "Jumps in the soil."},
]

ENV_EVENT_CARDS = [
    {"name": "Drought", "effect": "Lose 1 Producer unless adapted.", "type": "drought"},
    {"name": "Disease Outbreak", "effect": "Lose 1 Consumer unless adapted.", "type": "disease"},
    {"name": "Flood", "effect": "Lose 1 Decomposer unless adapted.", "type": "flood"},
    {"name": "Invasive Species", "effect": "Lose 1 random species.", "type": "invasive"},
    {"name": "Heat Wave", "effect": "Lose 1 Producer unless adapted.", "type": "heat"},
    {"name": "Cold Snap", "effect": "Lose 1 Consumer unless adapted.", "type": "cold"},
    {"name": "Pollution", "effect": "Lose 1 Decomposer unless adapted.", "type": "pollution"},
    {"name": "Fire", "effect": "Lose 1 species unless adapted.", "type": "fire"},
    {"name": "Pesticide Drift", "effect": "Lose 1 Insect unless adapted.", "type": "pesticide"},
    {"name": "Storm", "effect": "Lose 1 random species.", "type": "storm"},
    {"name": "Habitat Loss", "effect": "Lose 1 species from your largest habitat.", "type": "habitat_loss"},
    {"name": "Eutrophication", "effect": "Lose 1 Aquatic species unless adapted.", "type": "eutrophication"},
]

ADAPTATION_TOKENS = [
    "Drought Tolerance", "Disease Resistance", "Flood Survival", "Fire Resistance", "Cold Tolerance",
    "Heat Tolerance", "Pollution Resistance", "Pesticide Resistance", "Storm Survival", "Generalist"
]

RESOURCE_TYPES = ["Sunlight", "Water", "Nutrients"]

MAX_ROUNDS = 10



class Player:
    def __init__(self, name):
        self.name = name
        self.ecosystem = [] 
        self.connections = []
        self.adaptations = {}  
        self.resources = {"Sunlight": 2, "Water": 2, "Nutrients": 2}
        self.biodiversity_points = 0
        self.hand = []
    
    def add_species(self, card):
        self.ecosystem.append(card)
    
    def remove_species(self, card):
        if card in self.ecosystem:
            self.ecosystem.remove(card)
            if card["name"] in self.adaptations:
                del self.adaptations[card["name"]]
    
    def has_adaptation(self, species_name, adaptation):
        return adaptation in self.adaptations.get(species_name, [])
    
    def add_adaptation(self, species_name, adaptation):
        if species_name not in self.adaptations:
            self.adaptations[species_name] = []
        self.adaptations[species_name].append(adaptation)
    
    def count_species_type(self, type_):
        return sum(1 for c in self.ecosystem if c["type"] == type_)

    def unique_species(self):
        return len({c["name"] for c in self.ecosystem})
    
    def trophic_levels(self):
        return set(c["type"] for c in self.ecosystem)
    
    def ecosystem_summary(self):
        summary = f"\n{self.name}'s Ecosystem:\n"
        for c in self.ecosystem:
            adaps = ", ".join(self.adaptations.get(c["name"], []))
            summary += f" - {c['name']} ({c['type']}, {c['habitat']})"
            if adaps:
                summary += f" [Adaptations: {adaps}]"
            summary += "\n"
        summary += f"Connections: {len(self.connections)}"
        summary += f"\nResources: {self.resources}"
        summary += f"\nBiodiversity Points: {self.biodiversity_points}\n"
        return summary



def draw_species(deck, n=1):
    drawn = []
    for _ in range(n):
        if deck:
            drawn.append(deck.pop())
    return drawn

def draw_event(deck):
    if deck:
        return deck.pop()
    return None

def collect_resources(player):
    count_producers = player.count_species_type("Producer")
    count_decomposers = player.count_species_type("Decomposer")
    player.resources["Sunlight"] += count_producers
    player.resources["Nutrients"] += count_decomposers
    player.resources["Water"] += random.choice([1, 2])
    print(f"{player.name} collects resources: Sunlight+{count_producers}, Nutrients+{count_decomposers}, Water+1/2")

def can_place_species(player, card):
    if card["type"] == "Producer":
        return player.resources["Sunlight"] >= 1
    else:
        return all(player.resources[r] >= 1 for r in RESOURCE_TYPES)

def pay_for_species(player, card):
    if card["type"] == "Producer":
        player.resources["Sunlight"] -= 1
    else:
        for r in RESOURCE_TYPES:
            player.resources[r] -= 1

def place_species(player):
    print(f"{player.name}, your hand:")
    for idx, card in enumerate(player.hand):
        print(f"{idx+1}. {card['name']} ({card['type']}, {card['habitat']})")
    try:
        choice = int(input("Choose a species to place (number): ")) - 1
        card = player.hand[choice]
    except:
        print("Invalid choice.")
        return
    if can_place_species(player, card):
        pay_for_species(player, card)
        player.add_species(card)
        print(f"{card['name']} added to your ecosystem!")
        player.hand.pop(choice)
    else:
        print("Not enough resources to place this species.")

def create_connection(player):
    if len(player.ecosystem) < 2:
        print("Not enough species to create a connection!")
        return
    print("Your species:")
    for i, c in enumerate(player.ecosystem):
        print(f"{i+1}. {c['name']} ({c['type']})")
    try:
        idx1 = int(input("Choose first species (number): ")) - 1
        idx2 = int(input("Choose second species (number): ")) - 1
        if idx1 == idx2:
            print("Choose two different species.")
            return
        type_ = input("Type of connection (foodweb/symbiosis): ").lower()
        if type_ not in ("foodweb", "symbiosis"):
            print("Invalid connection type.")
            return
        c1 = player.ecosystem[idx1]
        c2 = player.ecosystem[idx2]
        player.connections.append((c1["name"], c2["name"], type_))
        print(f"Created {type_} connection between {c1['name']} and {c2['name']}")
    except:
        print("Invalid input.")

def acquire_adaptation(player, adaptation_pool):
    if not adaptation_pool:
        print("No adaptation tokens left.")
        return
    print(f"Available adaptations: {', '.join(adaptation_pool)}")
    choice = input("Which adaptation to acquire? ").strip()
    if choice not in adaptation_pool:
        print("Adaptation not available.")
        return
    if sum(player.resources.values()) < 2:
        print("Not enough resources to acquire adaptation.")
        return
    res_spent = 0
    for r in RESOURCE_TYPES:
        while player.resources[r] > 0 and res_spent < 2:
            player.resources[r] -= 1
            res_spent += 1
    adaptation_pool.remove(choice)
    print(f"Adaptation {choice} acquired.")
    print("Species in your ecosystem:")
    for i, c in enumerate(player.ecosystem):
        print(f"{i+1}. {c['name']}")
    try:
        idx = int(input("Which species to apply adaptation to? (number): ")) - 1
        species = player.ecosystem[idx]
        player.add_adaptation(species["name"], choice)
        print(f"{choice} applied to {species['name']}.")
    except:
        print("Invalid input.")

def resolve_event(player, event):
    print(f"{player.name} faces event: {event['name']} - {event['effect']}")
    affected = []
    if event["type"] == "drought":
        affected = [c for c in player.ecosystem if c["type"] == "Producer" and not player.has_adaptation(c["name"], "Drought Tolerance")]
    elif event["type"] == "disease":
        affected = [c for c in player.ecosystem if "Consumer" in c["type"] and not player.has_adaptation(c["name"], "Disease Resistance")]
    elif event["type"] == "flood":
        affected = [c for c in player.ecosystem if c["type"] == "Decomposer" and not player.has_adaptation(c["name"], "Flood Survival")]
    elif event["type"] == "heat":
        affected = [c for c in player.ecosystem if c["type"] == "Producer" and not player.has_adaptation(c["name"], "Heat Tolerance")]
    elif event["type"] == "cold":
        affected = [c for c in player.ecosystem if "Consumer" in c["type"] and not player.has_adaptation(c["name"], "Cold Tolerance")]
    elif event["type"] == "pollution":
        affected = [c for c in player.ecosystem if c["type"] == "Decomposer" and not player.has_adaptation(c["name"], "Pollution Resistance")]
    elif event["type"] == "fire":
        affected = [c for c in player.ecosystem if not player.has_adaptation(c["name"], "Fire Resistance")]
    elif event["type"] == "pesticide":
        insects = ["Bee", "Beetle", "Butterfly", "Grasshopper", "Ant", "Mantis", "Spider"]
        affected = [c for c in player.ecosystem if c["name"] in insects and not player.has_adaptation(c["name"], "Pesticide Resistance")]
    elif event["type"] == "storm":
        affected = [c for c in player.ecosystem if not player.has_adaptation(c["name"], "Storm Survival")]
    elif event["type"] == "habitat_loss":
        hab_counts = {}
        for c in player.ecosystem:
            hab_counts[c["habitat"]] = hab_counts.get(c["habitat"], 0) + 1
        if hab_counts:
            max_hab = max(hab_counts, key=hab_counts.get)
            affected = [c for c in player.ecosystem if c["habitat"] == max_hab]
    elif event["type"] == "eutrophication":
        aquatic = ["Wetland"]
        affected = [c for c in player.ecosystem if c["habitat"] in aquatic and not player.has_adaptation(c["name"], "Generalist")]
    elif event["type"] == "invasive":
        affected = player.ecosystem
    if affected:
        lost = random.choice(affected)
        player.remove_species(lost)
        print(f"{player.name} lost species: {lost['name']} due to {event['name']}!")
    else:
        print(f"{player.name} avoided losses thanks to adaptations!")

def gain_biodiversity_points(player):
    points = player.unique_species()
    points += len(player.connections)
    types_present = [c["type"] for c in player.ecosystem]
    if all(t in types_present for t in ["Producer", "Primary Consumer", "Secondary Consumer", "Decomposer"]):
        points += 2
    points += sum(len(adaps) for adaps in player.adaptations.values())
    player.biodiversity_points = points

def show_scoreboard(players):
    print("\n--- BIODIVERSITY SCOREBOARD ---")
    for p in players:
        print(f"{p.name}: {p.biodiversity_points} points")
    print("------------------------------\n")

def end_game(players):
    print("\nGAME OVER!")
    print("Final Scores:")
    show_scoreboard(players)
    winner = max(players, key=lambda p: p.biodiversity_points)
    print(f"Congratulations, {winner.name}! You created the most successful ecosystem!")
    exit()


def main():
    print("Welcome to EcoSystems: The Ecology Board Game (Python Edition)!")
    num_players = 0
    while num_players not in [2, 3, 4]:
        try:
            num_players = int(input("How many players? (2-4): "))
        except:
            continue
    players = []
    for i in range(num_players):
        pname = input(f"Enter name for Player {i+1}: ")
        players.append(Player(pname))
    deck = SPECIES_CARDS[:]
    random.shuffle(deck)
    for p in players:
        p.hand = draw_species(deck, 5)
        producers = [c for c in p.hand if c["type"] == "Producer"]
        if producers:
            start_card = producers[0]
            p.add_species(start_card)
            print(f"{p.name} starts with {start_card['name']} in ecosystem.")
            p.hand.remove(start_card)
        else:
            p.add_species(p.hand[0])
            print(f"{p.name} starts with {p.hand[0]['name']} in ecosystem.")
            p.hand.pop(0)
    events = ENV_EVENT_CARDS[:]
    random.shuffle(events)
    adaptation_pool = ADAPTATION_TOKENS[:]
    round_num = 1
    while round_num <= MAX_ROUNDS and events:
        print(f"\n======== ROUND {round_num} ========")
        for p in players:
            print(p.ecosystem_summary())
            print(f"{p.name}'s turn:")
            collect_resources(p)
            
            actions = ['draw', 'place', 'connect', 'adapt', 'end']
            actions_chosen = []
            for _ in range(2):
                print("\nActions: draw, place, connect, adapt, end")
                act = input("Choose action (or type 'end' to stop and see the winner): ").strip().lower()
                if act == "end":
                    end_game(players)
                elif act == "draw":
                    new_card = draw_species(deck)
                    if new_card:
                        p.hand += new_card
                        print(f"Drew species: {new_card[0]['name']}")
                    else:
                        print("Species deck is empty.")
                elif act == "place":
                    if p.hand:
                        place_species(p)
                    else:
                        print("Hand is empty.")
                elif act == "connect":
                    create_connection(p)
                elif act == "adapt":
                    acquire_adaptation(p, adaptation_pool)
                else:
                    print("Invalid action.")
                actions_chosen.append(act)
            if round_num % 2 == 0 and events:
                event = draw_event(events)
                print(f"\nEnvironmental Event: {event['name']} - {event['effect']}")
                resolve_event(p, event)
            gain_biodiversity_points(p)
            print(p.ecosystem_summary())
        show_scoreboard(players)
        round_num += 1
    end_game(players)

if __name__ == "__main__":
    main()