import os
import json

def build_data():
    # 1. Gather all files
    old_files = sorted(os.listdir('old'))
    mid_files = sorted(os.listdir('mid'))
    mid2_files = sorted(os.listdir('mid 2'))
    f2027_files = sorted(os.listdir('2027'))
    mp4_files = sorted(os.listdir('.MP4'))

    # Curated items with expressions, attacks, and Pinterest vibe
    items = []

    # CHAPTER 1: OLD
    old_metadata = {
        "2026_10_12_12_24_39_IMG_5310.JPG": {
            "title": "The Family Reunion Masterpiece",
            "caption": "Recreated with perfection. Sitting in the park with the whole squad, flowers in hand, and maximum main character poise.",
            "expression": "Serene elder sibling dominance. 100% calm while sibling wears bright yellow.",
            "vibe": "royal",
            "attack": "WHOLESOME OVERDRIVE 🌻",
            "tags": ["#FamilyCore", "#RecreationMastery", "#ParkDay", "#StoryOfMyLife"]
        },
        "2026_10_12_12_24_42_IMG_5279.JPG": {
            "title": "Little Flower Girl Era",
            "caption": "Pasted into the family album with glitter tape! Holding flowers like an official royal ambassador.",
            "expression": "Sweet innocent smile hiding mastermind mischievous intentions.",
            "vibe": "cute",
            "attack": "CUTENESS EMBARGO 🌸",
            "tags": ["#VintageAlbum", "#FlowerGirl", "#OriginStory", "#GlitterTape"]
        },
        "2026_10_12_12_34_54_IMG_5295.JPG": {
            "title": "Kashmiri Royalty with Sibling Sidekick",
            "caption": "Full traditional embroidered Kashmiri pheran and silver headpiece. Sibling standing by for backup.",
            "expression": "Regal mountain princess gaze. Looking down upon the valley with absolute authority.",
            "vibe": "royal",
            "attack": "MOUNTAIN AURA +5000 🏔️",
            "tags": ["#KashmiriGlam", "#MountainVibes", "#SiblingDuo", "#TraditionalSlay"]
        },
        "2026_10_12_12_34_54_IMG_5296.JPG": {
            "title": "Silver Jewelry Supremacy",
            "caption": "The traditional silver headpiece jingling in the breeze. Pure heritage chic.",
            "expression": "Contemplative vintage beauty in full 2000s glory.",
            "vibe": "royal",
            "attack": "SILVER QUEEN 👑",
            "tags": ["#HeritageGlam", "#Tradition", "#PureVibes", "#Iconic"]
        },
        "2026_10_12_12_34_57_IMG_5298.JPG": {
            "title": "The Fort Wall Shenanigans",
            "caption": "Sitting on the historic stone ramparts by the seaside harbor. White ruffled shirt and red pants.",
            "expression": "Calculated smile: 'If you push me, I am telling mom immediately.'",
            "vibe": "goofy",
            "attack": "SIBLING PLOT THICKENS 🏰",
            "tags": ["#FortressExplorer", "#HarborViews", "#SiblingDrama", "#Classic"]
        },
        "2026_10_12_12_34_58_IMG_5308.JPG": {
            "title": "Sibling WWE Champion Trophy",
            "caption": "Lifting the younger sibling horizontally like an Olympic gold medal or a championship belt.",
            "expression": "Triumphant grin holding hostage. Peak big sister supremacy.",
            "vibe": "chaotic",
            "attack": "WWE SLAM ATTACK 💥",
            "tags": ["#WWESibling", "#HostageSituation", "#TrophyBrother", "#ChaosMode"]
        },
        "2026_10_12_15_22_08_IMG_5232.JPG": {
            "title": "The Iconic Cheek-Touch Pose",
            "caption": "Finger gently touching cheek in traditional Kashmiri red robe and silver bells. A pose ahead of its time.",
            "expression": "Cheeky smirk: 'I know I am the favorite child and nobody can deny it.'",
            "vibe": "sassy",
            "attack": "CHEEK PINCH HAZARD 🍓",
            "tags": ["#ModelPose", "#CheekySmirk", "#KashmiriElegance", "#FavoriteChild"]
        },
        "2026_10_12_15_22_08_IMG_5233.JPG": {
            "title": "The 'I Did Not Eat The Sweets' Face",
            "caption": "Caught on camera looking remarkably innocent despite circumstantial evidence.",
            "expression": "100% Angelic cover-up face. Sugar rush suppressed.",
            "vibe": "cute",
            "attack": "INNOCENCE FEIGNED 🍰",
            "tags": ["#AngelChild", "#SweetTooth", "#NotGuilty", "#Flashback"]
        },
        "2026_10_12_15_22_08_IMG_5234.JPG": {
            "title": "Rapunzel Has Entered The Chat",
            "caption": "Cascading dark wavy tresses reaching past the waist, rich royal blue velvet choli with gold zari.",
            "expression": "Sweet composed poise. Hair game was already legendary at this tender age.",
            "vibe": "royal",
            "attack": "HAIRCARE AMBASSADOR 💇‍♀️",
            "tags": ["#RapunzelEra", "#VelvetGlamour", "#HairGoals", "#DesiPrincess"]
        },
        "2026_10_12_15_22_08_IMG_5235.JPG": {
            "title": "School Star & Master Prankster",
            "caption": "Looking like the smartest kid in class who secretly organizes the cafeteria revolution.",
            "expression": "Calm, polite exterior with a twinkle of impending mischief in the eyes.",
            "vibe": "sassy",
            "attack": "PRANK MASTER ALARM 🚨",
            "tags": ["#TopStudent", "#SecretMischief", "#CoreMemory", "#Throwback"]
        },
        "2026_10_12_15_22_10_IMG_5236.JPG": {
            "title": "Mid-Giggle Supernova",
            "caption": "Caught completely off guard in the middle of an uncontrollable giggle fit.",
            "expression": "Pure unadulterated joy that could light up a blackout.",
            "vibe": "goofy",
            "attack": "GIGGLE NUKE 💣",
            "tags": ["#PureJoy", "#MidCackle", "#Unfiltered", "#Happiness"]
        },
        "2026_10_12_15_22_10_IMG_5237.JPG": {
            "title": "Festive Sparkle Mascot",
            "caption": "Celebration day dressed to impress all the relatives and collect all the blessings (and cash).",
            "expression": "Festive excitement dialed up to 200%. Ready for sweets.",
            "vibe": "cute",
            "attack": "SPARKLE BLAST 🎆",
            "tags": ["#FestivalDay", "#DiwaliVibes", "#PocketMoneySecured", "#GoldenMemory"]
        },
        "2026_10_12_15_22_10_IMG_5238.JPG": {
            "title": "Mountain Mist & Purple Knit",
            "caption": "Standing by the red hillside railing overlooking misty mountain peaks in a bright purple sweater and blue scarf.",
            "expression": "Freezing cold in the mountain air but refusing to drop the smile.",
            "vibe": "cute",
            "attack": "WINTER SASS ❄️",
            "tags": ["#HillStation", "#PurpleVibe", "#MistyMountain", "#TravelDiaries"]
        },
        "2026_10_12_15_22_10_IMG_5239.JPG": {
            "title": "Vacation Boss Mode",
            "caption": "Family holiday scenic point. Standing proudly like she personally commissioned the view.",
            "expression": "Proud tourist stance: 'Yes, this mountain meets my standards.'",
            "vibe": "sassy",
            "attack": "TOURIST BOSS 🏖️",
            "tags": ["#VacationEra", "#ScenicOverlook", "#Explorer", "#LivingHerBestLife"]
        }
    }

    for f in old_files:
        meta = old_metadata.get(f, {
            "title": f"Vintage Memory #{f[-8:-4]}",
            "caption": "A golden throwback from the childhood archives.",
            "expression": "Sweet throwback smile.",
            "vibe": "cute",
            "attack": "NOSTALGIA BEAM 💫",
            "tags": ["#Vintage", "#OldDays", "#Throwback"]
        })
        items.append({
            "id": f"old_{f}",
            "src": f"old/{f}",
            "folder": "old",
            "era": 1,
            "eraKey": "old",
            "eraName": "Chapter 1: The Old Days",
            "title": meta["title"],
            "caption": meta["caption"],
            "expression": meta["expression"],
            "vibe": meta["vibe"],
            "attack": meta["attack"],
            "tags": meta["tags"],
            "likes": 240 + len(items) * 11
        })

    # CHAPTER 2: MID
    mid_metadata = {
        "2026_10_12_12_24_41_IMG_5273.JPG": {
            "title": "Sunset Beach Silhouette",
            "caption": "Standing by the ocean shore at sunset in embroidered cream and royal blue. Hair in high bun.",
            "expression": "Contemplating the entire universe, deep poetry, and what's for dinner.",
            "vibe": "royal",
            "attack": "POETIC DAMAGE 🌅",
            "tags": ["#SunsetSilhouette", "#OceanBreeze", "#GoldenHour", "#MainCharacter"]
        },
        "2026_10_12_12_24_42_IMG_5276.JPG": {
            "title": "Traditional Glow-Up Debut",
            "caption": "Festive ethnic wear radiating elegance. The transition from childhood mischief to poised young lady.",
            "expression": "Gentle confident warmth. Mastering the art of the camera smile.",
            "vibe": "royal",
            "attack": "ROYAL CHARISMA 💫",
            "tags": ["#GlowUp", "#EthnicWear", "#Elegance", "#MidEra"]
        },
        "2026_10_12_12_24_42_IMG_5278.JPG": {
            "title": "Sunlit Breeze & Radiance",
            "caption": "Out in the natural sunlight where golden hour does all the heavy lifting.",
            "expression": "Natural radiance. Skin glowing, hair blowing, worries disappearing.",
            "vibe": "cute",
            "attack": "VITAMIN D ATTACK ☀️",
            "tags": ["#GoldenHour", "#NaturalGlow", "#Breezy", "#WarmVibes"]
        },
        "2026_10_12_12_24_43_IMG_5281.JPG": {
            "title": "Chai & Conversations",
            "caption": "Evening cafe mood. Relaxed vibes with the group.",
            "expression": "Subtle smirk of someone who successfully dodged paying for fries.",
            "vibe": "sassy",
            "attack": "CHAI CHRONICLES ☕",
            "tags": ["#CafeHangout", "#ChaiTime", "#EveningChills", "#SassyQueen"]
        },
        "2026_10_12_15_15_54_IMG_5201.JPG": {
            "title": "Red Carpet Runway Stride",
            "caption": "Sunny yellow cold-shoulder kurta walking down the red carpet canopy hallway like it's Milan Fashion Week.",
            "expression": "Walk like the paparazzi are in the bushes. High fashion catwalk strut.",
            "vibe": "sassy",
            "attack": "CATWALK SMASH 💃",
            "tags": ["#RedCarpet", "#YellowKurti", "#RunwayModel", "#WeddingGuestSlay"]
        },
        "2026_10_12_15_15_55_IMG_5203.JPG": {
            "title": "The Party Sparkle",
            "caption": "Surrounded by celebrations and vibrant colors.",
            "expression": "Laughing because someone tripped and made it 10x funnier.",
            "vibe": "goofy",
            "attack": "CHAOS VIBES 🦋",
            "tags": ["#PartyTime", "#FestiveMood", "#CandidSmile", "#GoodVibes"]
        },
        "2026_10_12_15_15_55_IMG_5204.JPG": {
            "title": "The Certified Offensive Side-Eye",
            "caption": "Caught the exact micro-second someone said something completely absurd.",
            "expression": "Criminal offensive side-eye. 999 emotional damage dealt without speaking a word.",
            "vibe": "sassy",
            "attack": "CRIMINAL SIDE-EYE 👀",
            "tags": ["#SideEyeSlay", "#CaughtIn4K", "#SassyFace", "#UnimpressedQueen"]
        },
        "2026_10_12_15_15_55_IMG_5205.JPG": {
            "title": "Pinterest Aesthetic Selfie",
            "caption": "Soft focus, warm lighting, dream girl aesthetic.",
            "expression": "Gentle, soft aesthetic gaze. Certified Pinterest pin material.",
            "vibe": "cute",
            "attack": "SOFT GLOW BOMB 🌸",
            "tags": ["#PinterestGirl", "#SoftGlam", "#Aesthetic", "#Dreamy"]
        },
        "2026_10_12_15_15_55_IMG_5206.JPG": {
            "title": "Goa Beach Umbrella Chill",
            "caption": "Sitting under the colorful red sunshade on the beach sands, embroidered white dress, golden necklace.",
            "expression": "Vacation zen. Not answering any emails or phone calls.",
            "vibe": "cute",
            "attack": "BEACHSIDE SLAY 🏖️",
            "tags": ["#BeachVibes", "#GoaDiaries", "#UnderTheUmbrella", "#ChillPill"]
        },
        "2026_10_12_15_15_55_IMG_5207.JPG": {
            "title": "Sun-Kissed Golden Hour",
            "caption": "Filtered golden afternoon light creating an ethereal halo.",
            "expression": "Face card unconditionally accepted across international waters.",
            "vibe": "royal",
            "attack": "AURA +8,000 ✨",
            "tags": ["#GoldenHour", "#AuraFarming", "#Flawless", "#NoFilterNeeded"]
        },
        "2026_10_12_15_15_55_IMG_5209.JPG": {
            "title": "Casual Walk in Town",
            "caption": "Every sidewalk is a potential runway if you have enough confidence.",
            "expression": "Focused, stylish, minding her own fabulous business.",
            "vibe": "sassy",
            "attack": "STREETSTYLE ATTACK 👟",
            "tags": ["#StreetStyle", "#CasualChic", "#WalkTheWalk", "#OnTheMove"]
        },
        "2026_10_12_15_15_55_IMG_5210.JPG": {
            "title": "The Knowing Smirk & Lace Collar",
            "caption": "Intricate white lace choker neckline, cascading curls, chin rested thoughtfully on fingers.",
            "expression": "100% Knowing Smirk: 'I knew the gossip before you even opened your mouth.'",
            "vibe": "sassy",
            "attack": "SMUG SMIRK OVERLOAD 😏",
            "tags": ["#LaceCollar", "#TeaMaster", "#SmugQueen", "#CloseUpPerfection"]
        },
        "2026_10_12_15_15_55_IMG_5211.JPG": {
            "title": "Coffee Table Musings",
            "caption": "Waiting for the iced caramel macchiato while looking photogenic.",
            "expression": "Patiently holding the pose until the camera clicks.",
            "vibe": "cute",
            "attack": "CAFFEINE POWER ☕",
            "tags": ["#CoffeeDate", "#AestheticCorner", "#CafeGram", "#Cute"]
        },
        "2026_10_12_15_15_55_IMG_5213.JPG": {
            "title": "The Micro-Smile",
            "caption": "A quick candid snap that ended up being an accidental cover shot.",
            "expression": "Subtle, demure, absolutely glowing with understated confidence.",
            "vibe": "cute",
            "attack": "SPARKLE EYE BEAM ✨",
            "tags": ["#MicroSmile", "#Candid", "#SparklingEyes", "#NaturalBeauty"]
        },
        "2026_10_12_15_15_55_IMG_5214.JPG": {
            "title": "Mid-Laugh Authentic Joy",
            "caption": "No posing, no rehearsing, just pure spontaneous laughter.",
            "expression": "Unfiltered happiness breaking through any attempt at being serious.",
            "vibe": "goofy",
            "attack": "LAUGH ATTACK 😂",
            "tags": ["#RealMoments", "#CandidLaugh", "#PureVibes", "#CoreMemory"]
        },
        "2026_10_12_15_15_55_IMG_5216.JPG": {
            "title": "Aesthetic Board Star",
            "caption": "Everything in the frame aligned to create perfection.",
            "expression": "Effortless composure that makes photography look easy.",
            "vibe": "royal",
            "attack": "BOARD SAVED 📌",
            "tags": ["#PinterestVibes", "#BoardWorthy", "#AestheticFeed", "#Iconic"]
        },
        "2026_10_12_15_17_21_IMG_5227.JPG": {
            "title": "The Low-Key Sunday Chill",
            "caption": "Relaxed in comfy loungewear, showing that casual is a lifestyle.",
            "expression": "Unbothered, hydrated, living in her own peaceful orbit.",
            "vibe": "cute",
            "attack": "COZY COMFORT 🛋️",
            "tags": ["#CozyVibes", "#WeekendMode", "#ChillDay", "#RealMe"]
        },
        "2026_10_12_15_17_21_IMG_5228.JPG": {
            "title": "The Detective Eyebrow",
            "caption": "That one single raised eyebrow that solves crimes and interrogates friends.",
            "expression": "'Are you sure about that explanation?' FBI agent level skepticism.",
            "vibe": "sassy",
            "attack": "INTERROGATION BEAM 🔍",
            "tags": ["#EyebrowRaise", "#DetectiveMode", "#DoubtIt", "#CaughtYou"]
        },
        "2026_10_12_15_22_05_IMG_5229.JPG": {
            "title": "Garden Pathway Bloom",
            "caption": "Out in the floral bushes showing the flowers how blooming is really done.",
            "expression": "Radiant outdoor charm in full daylight.",
            "vibe": "cute",
            "attack": "CHLOROPHYLL SASS 🌿",
            "tags": ["#GardenGirl", "#Blooming", "#NatureVibe", "#FreshAir"]
        },
        "2026_10_12_15_22_08_IMG_5230.JPG": {
            "title": "Sweater Weather Protocol",
            "caption": "Cozy knitwear season looking like a warm cup of cocoa personified.",
            "expression": "Bundled up and feeling like the main character in an indie film.",
            "vibe": "cute",
            "attack": "KNITWEAR K.O. 🧶",
            "tags": ["#SweaterSeason", "#Warmth", "#IndieFilm", "#AutumnVibes"]
        },
        "2026_10_12_15_22_08_IMG_5231.JPG": {
            "title": "Heart-Warming Smile",
            "caption": "Close-up portrait with the signature gentle gaze.",
            "expression": "Sweet, endearing warmth that brings a smile to everyone.",
            "vibe": "cute",
            "attack": "HEART POP 💕",
            "tags": ["#SweetestSmile", "#Warmth", "#FriendsForever", "#Cherished"]
        },
        "2026_10_12_15_22_10_IMG_5245.JPG": {
            "title": "Shaadi Glamour Guest Star",
            "caption": "Stealing the spotlight at the wedding reception with unmatched poise.",
            "expression": "Looking like royalty attending a state banquet.",
            "vibe": "royal",
            "attack": "WEDDING CRASHER SLAY 💎",
            "tags": ["#ShaadiSeason", "#GuestStar", "#Bling", "#DesiGlam"]
        },
        "2026_10_12_15_22_10_IMG_5246.JPG": {
            "title": "Night Lights Sparkle",
            "caption": "Evening celebration with fairy lights sparkling in the background.",
            "expression": "Joyful festive smile catching the lantern glow.",
            "vibe": "royal",
            "attack": "MIDNIGHT SPARKLE 🌟",
            "tags": ["#FairyLights", "#EveningMagic", "#Celebration", "#StarGaze"]
        }
    }

    for f in mid_files:
        meta = mid_metadata.get(f, {
            "title": f"Mid Era Chapter #{f[-8:-4]}",
            "caption": "A moment from the teen glow-up chapter.",
            "expression": "Charming and radiant gaze.",
            "vibe": "cute",
            "attack": "GLOW UP IMPACT ✨",
            "tags": ["#MidEra", "#GlowUp", "#Memories"]
        })
        items.append({
            "id": f"mid_{f}",
            "src": f"mid/{f}",
            "folder": "mid",
            "era": 2,
            "eraKey": "mid",
            "eraName": "Chapter 2: The Mid Era",
            "title": meta["title"],
            "caption": meta["caption"],
            "expression": meta["expression"],
            "vibe": meta["vibe"],
            "attack": meta["attack"],
            "tags": meta["tags"],
            "likes": 380 + len(items) * 14
        })

    # CHAPTER 3: MID 2
    mid2_metadata = {
        "2026_10_12_12_24_39_IMG_5269.JPG": {
            "title": "The Casual Park Catwalk",
            "caption": "Walking the cobblestone park trail like it's a private estate.",
            "expression": "Casual but determined: 'I walk with purpose and perfect posture.'",
            "vibe": "sassy",
            "attack": "RUNWAY STRIDE 👠",
            "tags": ["#ParkWalk", "#Catwalk", "#PostureGoals", "#Effortless"]
        },
        "2026_10_12_12_24_41_IMG_5274.JPG": {
            "title": "Hydrated & Unbothered",
            "caption": "Greenery surrounding, mind at ease, drama completely blocked.",
            "expression": "Serenity level 100. Toxic energy bounced right off.",
            "vibe": "cute",
            "attack": "PEACE OF MIND 🕊️",
            "tags": ["#Unbothered", "#InnerPeace", "#Greenery", "#Mindfulness"]
        },
        "2026_10_12_12_24_44_IMG_5284.JPG": {
            "title": "Main Character Energy Stance",
            "caption": "Posing with the certainty that the camera was invented just for this second.",
            "expression": "Direct eye contact. Zero hesitation, 100% confidence.",
            "vibe": "royal",
            "attack": "MAIN CHARACTER SHOCK ⚡",
            "tags": ["#MainCharacter", "#Commanding", "#Confidence", "#PowerStance"]
        },
        "2026_10_12_12_27_52_IMG_5287.JPG": {
            "title": "Passenger Princess Melodrama",
            "caption": "Staring out the car window listening to sad love songs like a movie protagonist.",
            "expression": "Dramatically gazing into the distance as if rain was about to start.",
            "vibe": "goofy",
            "attack": "CINEMATIC TEARS 🎬",
            "tags": ["#PassengerPrincess", "#MusicVideoVibes", "#Melodrama", "#CarDiaries"]
        },
        "2026_10_12_12_27_52_IMG_5289.JPG": {
            "title": "Sunglasses Indoors Supremacy",
            "caption": "Chunky black vintage sunglasses in the passenger seat with red tinted lips and hand on jaw.",
            "expression": "Peak unbothered glamour. Wearing sunglasses inside because the future is blinding.",
            "vibe": "sassy",
            "attack": "EMOTIONAL DAMAGE 💀",
            "tags": ["#SunglassesIndoors", "#VIPStatus", "#PoutGame", "#DangerousGlam"]
        },
        "2026_10_12_12_27_53_IMG_5291.JPG": {
            "title": "The Celebrity Disguise",
            "caption": "Adjusting the sunglasses angle: 'No autographs today, please respect my privacy.'",
            "expression": "Rockstar privacy defense mode. 10/10 sass.",
            "vibe": "sassy",
            "attack": "PAPARAZZI FLASH 📸",
            "tags": ["#NoAutographs", "#CelebrityDisguise", "#CoolGirl", "#ShadesOn"]
        },
        "2026_10_12_12_34_54_IMG_5293.JPG": {
            "title": "Sunshine Burst on the Trail",
            "caption": "Bright daylight illuminating the whole path, caught in a vibrant moment.",
            "expression": "Beaming with energy that could power the regional electric grid.",
            "vibe": "cute",
            "attack": "SOLAR FLARE ☀️",
            "tags": ["#SunshineEnergy", "#HighVoltage", "#ParkAdventure", "#Radiant"]
        },
        "2026_10_12_12_34_57_IMG_5297.JPG": {
            "title": "Wide Denim & Lee Cooper Drip",
            "caption": "Orange graphic tee, wide flared raw-hem blue jeans, white sneakers, white cross-body bag on brick pavers.",
            "expression": "Supreme Gen-Z streetwear dominance. Relaxed stance, confident gaze.",
            "vibe": "sassy",
            "attack": "DENIM DOMINANCE 👖",
            "tags": ["#Streetwear", "#WideJeans", "#Sneakerhead", "#CasualIcon"]
        },
        "2026_10_12_12_34_58_IMG_5304.JPG": {
            "title": "Fit Check: Flawless Victory",
            "caption": "Checking the outfit from head to toe before conquering the afternoon.",
            "expression": "Subtle nod: 'Yes, this outfit is indeed a 10 out of 10.'",
            "vibe": "sassy",
            "attack": "DRIP CHECK 100% 💧",
            "tags": ["#FitCheck", "#OOTD", "#StreetStyle", "#CertifiedSlay"]
        },
        "2026_10_12_12_34_58_IMG_5305.JPG": {
            "title": "Serotonin Boost Snapshot",
            "caption": "A quick snapshot that instantly cures bad days and lifts morale.",
            "expression": "Warm, sunny, wholesome grin.",
            "vibe": "cute",
            "attack": "SEROTONIN BOOST 🍬",
            "tags": ["#InstantMoodLift", "#Wholesome", "#SmileDaily", "#PureVibes"]
        },
        "2026_10_12_15_15_55_IMG_5218.JPG": {
            "title": "Spilling The Chai",
            "caption": "Mid-conversation at the table with the world's most entertaining stories.",
            "expression": "Leaning in: 'Okay wait, listen to what happened next...'",
            "vibe": "sassy",
            "attack": "TEA SPILL ☕",
            "tags": ["#GossipProtocol", "#Storytime", "#BestFriends", "#CafeTales"]
        },
        "2026_10_12_15_15_55_IMG_5220.JPG": {
            "title": "Indoor Radiance",
            "caption": "Light bouncing off walls and matching her bright aura.",
            "expression": "Welcoming, warm, and delightfully cheerful.",
            "vibe": "cute",
            "attack": "WARM HUG ATTACK 🫂",
            "tags": ["#WarmAura", "#Cheer", "#EverydayJoy", "#BrightMoments"]
        },
        "2026_10_12_15_17_21_IMG_5225.JPG": {
            "title": "Genetic Advantage Flex",
            "caption": "Looking like this on a random Tuesday without an hour of hair styling.",
            "expression": "Subtle flex: 'I woke up like this, genuinely.'",
            "vibe": "sassy",
            "attack": "GENETIC FLEX 💪",
            "tags": ["#NoFilter", "#NaturalFlex", "#Effortless", "#Winning"]
        },
        "2026_10_12_15_22_10_IMG_5244.JPG": {
            "title": "Midnight Craving Expedition",
            "caption": "Night out with the crew, searching for ice cream or street momos.",
            "expression": "Determined food expedition commander face.",
            "vibe": "goofy",
            "attack": "MIDNIGHT SNACK 🍟",
            "tags": ["#FoodHunt", "#NightSquad", "#LateNightRuns", "#HungryQueen"]
        },
        "2026_10_12_15_22_10_IMG_5250.JPG": {
            "title": "Enchanted Garden Terrace",
            "caption": "Under the soft yellow pavilion lights in the breezy night air.",
            "expression": "Fairy garden resident enjoying the peaceful midnight hours.",
            "vibe": "royal",
            "attack": "FAIRY DUST ✨",
            "tags": ["#NightGarden", "#LanternGlow", "#Enchanted", "#Breezy"]
        },
        "2026_10_12_15_22_10_IMG_5251.JPG": {
            "title": "Cafe Terrace Strategist",
            "caption": "Reviewing the food menu with the focus of a grandmaster chess player.",
            "expression": "Deciding between pasta, pizza, or ordering both.",
            "vibe": "goofy",
            "attack": "MENU DILEMMA 🍕",
            "tags": ["#MenuTactics", "#FoodLover", "#CafeNights", "#Decisions"]
        },
        "2026_10_12_15_22_10_IMG_5253.JPG": {
            "title": "Paisley & Patched Denim Swagger",
            "caption": "Illuminated garden boardwalk at night. Paisley bandana blouse, patchwork wide jeans, hands casually in pockets.",
            "expression": "Coolest girl in the venue. Effortless stance, zero tension.",
            "vibe": "sassy",
            "attack": "STREETWEAR TSUNAMI 🌊",
            "tags": ["#BandanaPrint", "#PatchworkDenim", "#NightOut", "#PeakStyle"]
        },
        "2026_10_12_15_22_10_IMG_5254.JPG": {
            "title": "The Secret Garden Corner",
            "caption": "Framed by lush foliage and glowing outdoor garden lamps.",
            "expression": "Soft, calm, breathing in the evening tranquility.",
            "vibe": "cute",
            "attack": "BREEZY CHARM 🍃",
            "tags": ["#GardenCorner", "#NightVibes", "#SoftAura", "#Tranquil"]
        },
        "2026_10_12_15_22_10_IMG_5256.JPG": {
            "title": "Starlight in Her Eyes",
            "caption": "Fairy lights reflected in her eyes like constellations.",
            "expression": "Enchanted look, dreamlike atmosphere.",
            "vibe": "royal",
            "attack": "STARLIGHT STRIKE ⭐",
            "tags": ["#StarlightEyes", "#Constellations", "#DreamyNights", "#Magic"]
        },
        "2026_10_12_15_22_10_IMG_5259.JPG": {
            "title": "High Fashion Shadow Play",
            "caption": "Dramatic outdoor lighting carving sharp aesthetic shadows.",
            "expression": "Editorial composure. Vogue could call any minute.",
            "vibe": "royal",
            "attack": "AESTHETIC CRUSH 🖤",
            "tags": ["#Editorial", "#ShadowPlay", "#VogueCover", "#Striking"]
        },
        "2026_10_12_15_22_10_IMG_5260.JPG": {
            "title": "The Mega-Watt Smile",
            "caption": "When the joke is so good you have to hold your stomach.",
            "expression": "100% wattage. Happiness uncontained.",
            "vibe": "goofy",
            "attack": "SMILE NUKE 😁",
            "tags": ["#MegawattSmile", "#GiggleFest", "#HeartOfGold", "#PureSun"]
        },
        "2026_10_12_15_22_10_IMG_5261.JPG": {
            "title": "Midnight Promenade",
            "caption": "Strolling under the starlit sky after a full day of adventures.",
            "expression": "Peaceful, content, glowing against the dark night sky.",
            "vibe": "cute",
            "attack": "MOONBEAM HIT 🌙",
            "tags": ["#NightWalk", "#Moonlit", "#Serene", "#GoodTimes"]
        },
        "2026_10_12_15_22_10_IMG_5262.JPG": {
            "title": "Warm Chai & Giggles",
            "caption": "Cozy warmth at the table with good friends and warm drinks.",
            "expression": "The comfort of great company and shared stories.",
            "vibe": "cute",
            "attack": "WARMTH WAVE ♨️",
            "tags": ["#FriendshipGoals", "#ChaiSips", "#HeartWarm", "#BestMoments"]
        },
        "2026_10_12_15_22_10_IMG_5264.JPG": {
            "title": "Hello Kitty Mall Enforcer",
            "caption": "Embroidered white Chikankari kurti at the mall with full Hello Kitty face stickers filter!",
            "expression": "Cute Hello Kitty cheeks vs internal desire to cause peaceful chaos.",
            "vibe": "goofy",
            "attack": "HELLO KITTY SLAP 🎀",
            "tags": ["#HelloKittyFilter", "#MallShenanigans", "#ChikankariKurti", "#CutestChaos"]
        }
    }

    for f in mid2_files:
        meta = mid2_metadata.get(f, {
            "title": f"Mid 2 Chapter #{f[-8:-4]}",
            "caption": "Peak sass and main character energy in motion.",
            "expression": "Sassy and confident stare.",
            "vibe": "sassy",
            "attack": "MAIN CHARACTER PULSE ⚡",
            "tags": ["#Mid2", "#PeakSass", "#Memories"]
        })
        items.append({
            "id": f"mid2_{f}",
            "src": f"mid 2/{f}",
            "folder": "mid 2",
            "era": 3,
            "eraKey": "mid2",
            "eraName": "Chapter 3: Peak Sass",
            "title": meta["title"],
            "caption": meta["caption"],
            "expression": meta["expression"],
            "vibe": meta["vibe"],
            "attack": meta["attack"],
            "tags": meta["tags"],
            "likes": 510 + len(items) * 16
        })

    # CHAPTER 4: 2027
    f2027_metadata = {
        "2026_10_12_12_24_39_IMG_5309.JPG": {
            "title": "The 2027 Coronation",
            "caption": "Reaching her ultimate royal form. Poise, dignity, and undeniable aura.",
            "expression": "Empress-level serenity. Knowing her place at the top.",
            "vibe": "royal",
            "attack": "CROWN JOULE 👑",
            "tags": ["#2027Era", "#Coronation", "#AuraUnstoppable", "#QueenBehavior"]
        },
        "2026_10_12_12_24_40_IMG_5270.JPG": {
            "title": "The Purple Lehenga on Flower Stairs",
            "caption": "Sitting gracefully on marble stairs draped in exotic purple orchids and yellow sunflowers, rich jacquard brocade lehenga, hands delicately adjusting hair.",
            "expression": "Goddess-level grace. Looking like the protagonist of a royal historical epic.",
            "vibe": "royal",
            "attack": "ROYAL LEHENGA SMASH 💜",
            "tags": ["#PurpleLehenga", "#FloralStaircase", "#RoyalEpic", "#C2Supremacy"]
        },
        "2026_10_12_12_24_40_IMG_5272.JPG": {
            "title": "Staircase Floral Symphony",
            "caption": "Full view of the cascading orchid garlands framing her purple brocade ensemble.",
            "expression": "Calm, majestic composure. Every single detail on point.",
            "vibe": "royal",
            "attack": "FLOWER BOMB 🌸",
            "tags": ["#FloralElegance", "#MasterpiecePhoto", "#RegalVibes", "#Iconic"]
        },
        "2026_10_12_12_24_42_IMG_5277.JPG": {
            "title": "Brocade & Whispers of Gold",
            "caption": "Close portrait on the decorated stairs. Pure silk sheen and gold zari work.",
            "expression": "A peaceful, contented half-smile that commands absolute respect.",
            "vibe": "royal",
            "attack": "SILK WHISPER ✨",
            "tags": ["#SilkAndZari", "#TraditionalQueen", "#GoldenGlow", "#2027"]
        },
        "2026_10_12_12_24_43_IMG_5280.JPG": {
            "title": "The Golden Celebration",
            "caption": "Surrounded by celebrations and festival lights.",
            "expression": "Illuminated by festival joy, glowing from within.",
            "vibe": "royal",
            "attack": "GOLDEN BLESSING 🪙",
            "tags": ["#Celebration2027", "#FestiveGold", "#Royalty", "#Joy"]
        },
        "2026_10_12_12_24_44_IMG_5283.JPG": {
            "title": "Timeless Festive Charm",
            "caption": "A candid instant where tradition meets contemporary grace.",
            "expression": "Gentle, captivating expression that stops time.",
            "vibe": "cute",
            "attack": "TIMELESS STRIKE ⏳",
            "tags": ["#TimelessBeauty", "#DesiElegance", "#Graceful", "#Loved"]
        },
        "2026_10_12_12_27_52_IMG_5288.JPG": {
            "title": "Car Window Golden Halo",
            "caption": "Sunbeams through the front windshield creating an angelic golden contour.",
            "expression": "Golden hour passenger bliss. Effortless glow.",
            "vibe": "cute",
            "attack": "SUNSHINE LASER ⚡",
            "tags": ["#GoldenHourCar", "#SunbeamHalo", "#NaturalAura", "#Glow"]
        },
        "2026_10_12_12_34_57_IMG_5300.JPG": {
            "title": "The Emerald Garden Radiance",
            "caption": "Deep bottle-green anarkali with mirror embroidery standing in tropical sunshine.",
            "expression": "Radiant outdoor elegance outshining the midday sun.",
            "vibe": "royal",
            "attack": "EMERALD CRUSH 💚",
            "tags": ["#EmeraldGreen", "#GardenGlow", "#SunshineQueen", "#DesiCouture"]
        },
        "2026_10_12_12_34_57_IMG_5301.JPG": {
            "title": "Jhumkas & Emerald Elegance",
            "caption": "Traditional gold jhumkas and bead necklace framing a serene portrait under the blue sky.",
            "expression": "Shy, dazzling smile with sparkling eyes.",
            "vibe": "cute",
            "attack": "JHUMKA JAB 💎",
            "tags": ["#JhumkaLove", "#TraditionalJewelry", "#EmeraldSlay", "#PureGrace"]
        },
        "2026_10_12_12_34_58_IMG_5302.JPG": {
            "title": "Palm Tree Hair-Tuck Maneuver",
            "caption": "Standing beside a towering palm tree, gently tucking dark hair behind ear in embroidered emerald green.",
            "expression": "The hair-tuck maneuver: 100% effective, 0% counterplay. Lethal charm.",
            "vibe": "sassy",
            "attack": "HAIR FLIP CRITICAL HIT 🌴",
            "tags": ["#HairTuckLethal", "#PalmTreeChic", "#EmeraldMasterpiece", "#CriticalHit"]
        },
        "2026_10_12_12_34_58_IMG_5303.JPG": {
            "title": "Golden Sunlight Symphony",
            "caption": "Basking in the open sun with colorful bangles and intricate floral embroidery.",
            "expression": "Supreme comfort in her own skin. Aura points reaching infinity.",
            "vibe": "royal",
            "attack": "AURA +99,999 ☀️",
            "tags": ["#InfiniteAura", "#SunlitGoddess", "#FinalForm", "#Queen"]
        },
        "WhatsApp Image 2026-10-12 at 8.17.33 PM.jpeg": {
            "title": "The Royal Brocade Mirror Selfie",
            "caption": "Mirror selfie in full purple brocade lehenga and gold paisley dupatta. Phone in hand, henna on palms.",
            "expression": "Quiet pride: 'Look at this fit. I know for a fact I did that.'",
            "vibe": "royal",
            "attack": "MIRROR SELFIE SLAY 📱",
            "tags": ["#MirrorSelfieRoyal", "#PurpleBrocade", "#HennaArt", "#FitCheckFinal"]
        },
        "WhatsApp Image 2026-10-12 at 8.17.34 PM (1).jpeg": {
            "title": "Passenger Princess on Duty",
            "caption": "Looking into the lens during an afternoon road trip with soft lighting.",
            "expression": "Soft, captivating glance that effortlessly steals the scene.",
            "vibe": "cute",
            "attack": "HEART STEALER 💖",
            "tags": ["#PassengerPrincess", "#RoadTrip", "#SoftGlance", "#Pretty"]
        },
        "WhatsApp Image 2026-10-12 at 8.17.34 PM (2).jpeg": {
            "title": "Fresh Faced Natural Radiance",
            "caption": "Zero makeup needed when your smile lights up the interior of the car.",
            "expression": "Sweet, organic smile radiating friendliness.",
            "vibe": "cute",
            "attack": "ORGANIC RADIANCE 🌿",
            "tags": ["#NaturalVibe", "#FreshFaced", "#SweetSmile", "#Wholesome"]
        },
        "WhatsApp Image 2026-10-12 at 8.17.34 PM (3).jpeg": {
            "title": "The Car Giggle Explosion",
            "caption": "When someone makes a ridiculous joke while cruising on the highway.",
            "expression": "Uncontrollable car laughter, completely unable to keep a straight face.",
            "vibe": "goofy",
            "attack": "GIGGLE GRENADE 💥",
            "tags": ["#HighwayGiggles", "#CarChaos", "#LaughAttack", "#Besties"]
        },
        "WhatsApp Image 2026-10-12 at 8.17.34 PM (4).jpeg": {
            "title": "The Scrunchy-Face Gremlin Attack",
            "caption": "Eyes squeezed shut, teeth grinning wide, pink hearts floating above! The absolute pinnacle of goofy joy.",
            "expression": "1000% Goofy Gremlin energy! Face card did not decline, it cashed out completely!",
            "vibe": "goofy",
            "attack": "EMOTIONAL CRITICAL DAMAGE 🤪",
            "tags": ["#ScrunchyFace", "#HeartFilter", "#GremlinMode", "#AbsoluteGem"]
        },
        "WhatsApp Image 2026-10-12 at 8.17.34 PM.jpeg": {
            "title": "Car Seat Poise & Elegance",
            "caption": "Sitting in the car seat with graceful posture, head tilted just right.",
            "expression": "Calm, regal confidence even in traffic.",
            "vibe": "royal",
            "attack": "TILT POWER 📐",
            "tags": ["#HeadTilt", "#CarSeatGrace", "#EleganceInTraffic", "#Icon"]
        },
        "WhatsApp Image 2026-10-12 at 8.18.20 PM (1).jpeg": {
            "title": "The 45-Degree Master Angle",
            "caption": "Cascading brunette hair, striped linen blouse, captivating hazel eyes staring right into the soul.",
            "expression": "Mesmerizing warm brown eyes. Certified most lethal selfie in the database.",
            "vibe": "sassy",
            "attack": "ANGLE OF DOOM 📐✨",
            "tags": ["#MasterAngle", "#HazelGaze", "#HairCascade", "#LethalSelfie"]
        },
        "WhatsApp Image 2026-10-12 at 8.18.20 PM (2).jpeg": {
            "title": "Sunlit Honey Glow",
            "caption": "Warm honey tones caressing her smile as evening sets in.",
            "expression": "Sweet, contented, radiating pure sunshine.",
            "vibe": "cute",
            "attack": "SWEETNESS OVERLOAD 🍯",
            "tags": ["#HoneyGlow", "#SunlitSweetness", "#WarmEyes", "#Angel"]
        },
        "WhatsApp Image 2026-10-12 at 8.18.20 PM.jpeg": {
            "title": "The 2027 Visionary (Final Boss)",
            "caption": "The journey from childhood mischief to unstoppable queenhood is complete.",
            "expression": "Knowing she conquered the past, commands the present, and owns the future.",
            "vibe": "royal",
            "attack": "FINAL BOSS AURA 👑",
            "tags": ["#FinalBossAura", "#QueenOf2027", "#StoryComplete", "#Unmatched"]
        },
        "WhatsApp Video 2026-10-12 at 8.17.34 PM.mp4": {
            "title": "2027 Live Motion Memory",
            "caption": "Live motion capture of the iconic moments. Real laughter, real breeze.",
            "expression": "Real-time radiance in living motion graphics.",
            "vibe": "goofy",
            "attack": "MOTION BLUR SLAY 🎬",
            "tags": ["#LiveMotion", "#VideoMemory", "#LivingHistory", "#RealTime"]
        }
    }

    for f in f2027_files:
        meta = f2027_metadata.get(f, {
            "title": f"2027 Era Chapter #{f[:10]}",
            "caption": "The peak of beauty and confidence in the 2027 era.",
            "expression": "Radiant modern elegance.",
            "vibe": "royal",
            "attack": "FUTURE DOMINANCE 👑",
            "tags": ["#2027", "#FinalChapter", "#Queen"]
        })
        isVideo = f.lower().endswith(('.mp4', '.mov'))
        items.append({
            "id": f"2027_{f}",
            "src": f"2027/{f}",
            "folder": "2027",
            "era": 4,
            "eraKey": "2027",
            "eraName": "Chapter 4: 2027 & Beyond",
            "title": meta["title"],
            "caption": meta["caption"],
            "expression": meta["expression"],
            "vibe": meta["vibe"],
            "attack": meta["attack"],
            "tags": meta["tags"],
            "isVideo": isVideo,
            "likes": 640 + len(items) * 20
        })

    # Videos from .MP4 folder
    video_items = []
    for f in mp4_files:
        video_items.append({
            "id": f"mp4_{f}",
            "src": f".MP4/{f}",
            "folder": ".MP4",
            "era": 5,
            "eraKey": "motion",
            "eraName": "Live Motion Clips",
            "title": f"Live Motion Snippet {f[-8:-4]}",
            "caption": "Live video capture of candid laughter and memories.",
            "expression": "Living, breathing spontaneity in high-res motion.",
            "vibe": "goofy",
            "attack": "LIVE MOTION NUKE 📹",
            "tags": ["#LiveMotion", "#CandidVideo", "#StoryOfMyLife"],
            "isVideo": True,
            "likes": 880 + len(video_items) * 25
        })

    full_payload = {
        "song": {
            "title": "Story of My Life",
            "artist": "One Direction",
            "src": "vidssave.com One Direction - Story of My Life 128KBPS.mp4",
            "lyrics": [
                "Written in these walls are the stories that I can't explain...",
                "I leave my heart open, but it stays right here empty for days...",
                "She told me in the morning she don't feel the same about us in her bones...",
                "The story of my life, I take her home, I drive all night to keep her warm...",
                "And time is frozen... the story of, the story of my life!"
            ]
        },
        "eras": [
            {
                "id": "old",
                "step": 1,
                "name": "The Old Days",
                "subtitle": "The Origin Story & Vintage Chaos",
                "tagline": "Where the legend began: Traditional Kashmiri glam, sibling wrestling championships, and unbothered innocence.",
                "yearRange": "Childhood • Chapter 01",
                "color": "#E06D53",
                "badge": "👶 Chapter 1",
                "icon": "🧸"
            },
            {
                "id": "mid",
                "step": 2,
                "name": "The Mid Era",
                "subtitle": "The Teen Glow-Up & Beach Sunsets",
                "tagline": "Red carpet wedding walks, sunset silhouettes by the ocean, and the birth of the certified side-eye.",
                "yearRange": "Teen Years • Chapter 02",
                "color": "#D97706",
                "badge": "✨ Chapter 2",
                "icon": "🌅"
            },
            {
                "id": "mid2",
                "step": 3,
                "name": "Peak Sass & Shenanigans",
                "subtitle": "The Sunglasses & Main Character Arc",
                "tagline": "Oversized shades in the passenger seat, Hello Kitty mall photo ops, and wide denim streetwear dominance.",
                "yearRange": "Prime Era • Chapter 03",
                "color": "#8B5CF6",
                "badge": "🕶️ Chapter 3",
                "icon": "💅"
            },
            {
                "id": "2027",
                "step": 4,
                "name": "2027 & Beyond",
                "subtitle": "The Final Form: Royal Grace & Scrunchy Faces",
                "tagline": "Royal purple silk brocade on flower stairs, emerald green goddess vibes, and completely unhinged cute selfies.",
                "yearRange": "2027 & Beyond • Chapter 04",
                "color": "#EC4899",
                "badge": "👑 Chapter 4",
                "icon": "👑"
            }
        ],
        "items": items,
        "videos": video_items
    }

    with open('galleryData.js', 'w', encoding='utf-8') as f:
        f.write("window.STORY_DATA = " + json.dumps(full_payload, indent=2, ensure_ascii=False) + ";\n")

    print(f"Generated galleryData.js successfully with {len(items)} photos and {len(video_items)} motion clips!")

if __name__ == '__main__':
    build_data()
