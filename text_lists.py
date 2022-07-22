# let list_of_words = []
#
# for (let i = 0; i < document.querySelectorAll('.table__row').length; i++) { list_of_words.push(document.querySelectorAll('.table__row')[i].textContent.substring(0, 3))}

three_letter_words = [
    "aal",
    "aas",
    "aba",
    "abs",
    "aby",
    "ace",
    "ach",
    "ack",
    "act",
    "add",
    "ado",
    "ads",
    "adz",
    "aes",
    "aff",
    "aft",
    "aga",
    "age",
    "ago",
    "aha",
    "ahi",
    "ahs",
    "aid",
    "ail",
    "aim",
    "ain",
    "air",
    "ais",
    "ait",
    "aks",
    "ala",
    "alb",
    "ale",
    "all",
    "alp",
    "als",
    "alt",
    "ama",
    "ami",
    "amp",
    "amu",
    "ana",
    "and",
    "ane",
    "ani",
    "ant",
    "any",
    "ape",
    "app",
    "apt",
    "arb",
    "arc",
    "are",
    "arf",
    "ark",
    "arm",
    "ars",
    "art",
    "ash",
    "ask",
    "asp",
    "ass",
    "ate",
    "ats",
    "att",
    "auk",
    "ava",
    "ave",
    "avo",
    "awa",
    "awe",
    "awl",
    "awn",
    "aww",
    "axe",
    "aye",
    "ays",
    "azo",
    "baa",
    "bad",
    "bae",
    "bag",
    "bah",
    "bal",
    "bam",
    "ban",
    "bap",
    "bar",
    "bas",
    "bat",
    "bay",
    "bed",
    "bee",
    "beg",
    "bel",
    "ben",
    "bet",
    "bey",
    "bff",
    "bib",
    "bid",
    "big",
    "bin",
    "bio",
    "bis",
    "bit",
    "biz",
    "boa",
    "bob",
    "bod",
    "bog",
    "bon",
    "boo",
    "bop",
    "bos",
    "bot",
    "bow",
    "box",
    "boy",
    "bra",
    "bro",
    "brr",
    "bub",
    "bud",
    "bug",
    "bum",
    "bun",
    "bur",
    "bus",
    "but",
    "buy",
    "bye",
    "bys",
    "cab",
    "cad",
    "cam",
    "can",
    "cap",
    "car",
    "cat",
    "caw",
    "cay",
    "cee",
    "cel",
    "cep",
    "cha",
    "chi",
    "cig",
    "cis",
    "cob",
    "cod",
    "cog",
    "col",
    "con",
    "coo",
    "cop",
    "coq",
    "cor",
    "cos",
    "cot",
    "cow",
    "cox",
    "coy",
    "coz",
    "cru",
    "cry",
    "cub",
    "cud",
    "cue",
    "cup",
    "cur",
    "cut",
    "cwm",
    "dab",
    "dad",
    "dag",
    "dah",
    "dai",
    "dak",
    "dal",
    "dam",
    "dan",
    "dap",
    "daw",
    "day",
    "deb",
    "dee",
    "def",
    "del",
    "den",
    "der",
    "dev",
    "dew",
    "dex",
    "dey",
    "dhu",
    "dib",
    "did",
    "die",
    "dif",
    "dig",
    "dim",
    "din",
    "dip",
    "dis",
    "dit",
    "dob",
    "doc",
    "doe",
    "dog",
    "doh",
    "dol",
    "dom",
    "don",
    "dop",
    "dor",
    "dos",
    "dot",
    "dow",
    "dox",
    "dry",
    "dub",
    "dud",
    "due",
    "dug",
    "duh",
    "dui",
    "dum",
    "dun",
    "duo",
    "dup",
    "dur",
    "dux",
    "dye",
    "dzo",
    "ear",
    "eat",
    "eau",
    "ebb",
    "eco",
    "ecu",
    "edh",
    "eek",
    "eel",
    "eff",
    "efs",
    "eft",
    "egg",
    "ego",
    "eke",
    "eld",
    "elf",
    "elk",
    "ell",
    "elm",
    "els",
    "eme",
    "emf",
    "emo",
    "ems",
    "emu",
    "end",
    "eng",
    "ens",
    "eon",
    "era",
    "ere",
    "erf",
    "erg",
    "erk",
    "ern",
    "err",
    "ers",
    "ese",
    "esq",
    "ess",
    "eta",
    "eth",
    "eve",
    "ewe",
    "eww",
    "eye",
    "fab",
    "fad",
    "fah",
    "fan",
    "fap",
    "far",
    "fas",
    "fat",
    "fax",
    "fay",
    "fed",
    "fee",
    "feh",
    "fem",
    "fen",
    "fer",
    "fet",
    "feu",
    "few",
    "fey",
    "fez",
    "fib",
    "fid",
    "fie",
    "fig",
    "fil",
    "fin",
    "fir",
    "fit",
    "fix",
    "fiz",
    "flo",
    "flu",
    "fly",
    "fob",
    "foe",
    "fog",
    "foh",
    "fon",
    "foo",
    "fop",
    "for",
    "fou",
    "fox",
    "foy",
    "fro",
    "fry",
    "fub",
    "fud",
    "fug",
    "fun",
    "fur",
    "gab",
    "gad",
    "gae",
    "gag",
    "gah",
    "gak",
    "gal",
    "gam",
    "gan",
    "gap",
    "gar",
    "gas",
    "gat",
    "gay",
    "ged",
    "gee",
    "gel",
    "gem",
    "gen",
    "geo",
    "get",
    "gey",
    "ghi",
    "gib",
    "gid",
    "gie",
    "gig",
    "gin",
    "gip",
    "gis",
    "git",
    "gnu",
    "goa",
    "gob",
    "god",
    "goo",
    "gor",
    "got",
    "gox",
    "goy",
    "gua",
    "gub",
    "gul",
    "gum",
    "gun",
    "gur",
    "gut",
    "guv",
    "guy",
    "gym",
    "hac",
    "had",
    "hae",
    "hag",
    "hah",
    "hai",
    "haj",
    "ham",
    "hao",
    "hap",
    "has",
    "hat",
    "haw",
    "hay",
    "hed",
    "heh",
    "hem",
    "hen",
    "hep",
    "her",
    "hes",
    "het",
    "hew",
    "hex",
    "hey",
    "hic",
    "hid",
    "hie",
    "him",
    "hin",
    "hip",
    "his",
    "hit",
    "hmm",
    "hob",
    "hoc",
    "hod",
    "hoe",
    "hog",
    "hoi",
    "hok",
    "hom",
    "hon",
    "hop",
    "hos",
    "hot",
    "how",
    "hoy",
    "hub",
    "hue",
    "hug",
    "huh",
    "hui",
    "hum",
    "hun",
    "hup",
    "hut",
    "hyp",
    "ice",
    "ich",
    "ick",
    "icy",
    "ide",
    "ids",
    "iff",
    "ifs",
    "igg",
    "ilk",
    "ill",
    "imp",
    "imu",
    "ink",
    "inn",
    "ins",
    "ion",
    "ire",
    "irk",
    "ism",
    "ist",
    "itd",
    "its",
    "ivy",
    "iwi",
    "jab",
    "jag",
    "jai",
    "jam",
    "jar",
    "jaw",
    "jay",
    "jee",
    "jet",
    "jeu",
    "jib",
    "jig",
    "jim",
    "jin",
    "jit",
    "job",
    "joe",
    "jog",
    "jol",
    "jot",
    "jow",
    "joy",
    "jua",
    "jug",
    "jun",
    "jus",
    "jut",
    "kab",
    "kae",
    "kaf",
    "kai",
    "kas",
    "kat",
    "kay",
    "kea",
    "ked",
    "kef",
    "keg",
    "ken",
    "kep",
    "kes",
    "kex",
    "key",
    "khi",
    "kia",
    "kid",
    "kif",
    "kin",
    "kip",
    "kir",
    "kit",
    "koa",
    "kob",
    "koi",
    "kop",
    "kor",
    "kos",
    "kue",
    "kye",
    "kyu",
    "lab",
    "lac",
    "lad",
    "lag",
    "lah",
    "lam",
    "lap",
    "lar",
    "las",
    "lat",
    "lav",
    "law",
    "lax",
    "lay",
    "lea",
    "led",
    "lee",
    "leg",
    "lei",
    "lek",
    "let",
    "leu",
    "lev",
    "lex",
    "ley",
    "lib",
    "lid",
    "lie",
    "lig",
    "lin",
    "lip",
    "lis",
    "lit",
    "loa",
    "lob",
    "log",
    "loo",
    "lop",
    "loq",
    "lot",
    "low",
    "lox",
    "lsd",
    "lud",
    "lug",
    "lum",
    "lur",
    "luv",
    "lux",
    "lye",
    "maa",
    "mac",
    "mad",
    "mae",
    "mag",
    "mai",
    "mam",
    "man",
    "map",
    "mar",
    "mas",
    "mat",
    "maw",
    "max",
    "may",
    "mea",
    "med",
    "meg",
    "meh",
    "mel",
    "mem",
    "men",
    "mer",
    "met",
    "mew",
    "mho",
    "mib",
    "mic",
    "mid",
    "mig",
    "mil",
    "mim",
    "mir",
    "mis",
    "mix",
    "moa",
    "mob",
    "moc",
    "mod",
    "mog",
    "moi",
    "mol",
    "mom",
    "mon",
    "moo",
    "mop",
    "mor",
    "mos",
    "mot",
    "mow",
    "mud",
    "mug",
    "mum",
    "mun",
    "mus",
    "mut",
    "mux",
    "mwa",
    "nab",
    "nae",
    "nag",
    "nah",
    "nai",
    "nam",
    "nan",
    "nap",
    "naw",
    "nay",
    "neb",
    "ned",
    "nee",
    "nef",
    "nek",
    "nem",
    "net",
    "new",
    "nib",
    "nil",
    "nim",
    "nip",
    "nit",
    "nix",
    "nob",
    "nod",
    "nog",
    "noh",
    "nom",
    "non",
    "noo",
    "nor",
    "nos",
    "not",
    "now",
    "nth",
    "nub",
    "nun",
    "nus",
    "nut",
    "nux",
    "oaf",
    "oak",
    "oar",
    "oat",
    "oba",
    "obe",
    "obi",
    "obv",
    "oca",
    "och",
    "oda",
    "odd",
    "ode",
    "ods",
    "oer",
    "oes",
    "off",
    "oft",
    "ohm",
    "oho",
    "ohs",
    "ohu",
    "oik",
    "oil",
    "oka",
    "oke",
    "old",
    "ole",
    "olm",
    "oms",
    "one",
    "ono",
    "ons",
    "oof",
    "ooh",
    "oom",
    "oos",
    "oot",
    "ope",
    "ops",
    "opt",
    "ora",
    "orb",
    "orc",
    "ore",
    "orf",
    "ors",
    "ort",
    "ose",
    "oud",
    "our",
    "ous",
    "out",
    "ova",
    "ovo",
    "owe",
    "owl",
    "own",
    "owt",
    "oxo",
    "oxy",
    "pac",
    "pad",
    "pah",
    "pal",
    "pam",
    "pan",
    "pap",
    "par",
    "pas",
    "pat",
    "paw",
    "pax",
    "pay",
    "pea",
    "pec",
    "ped",
    "pee",
    "peg",
    "peh",
    "pen",
    "pep",
    "per",
    "pes",
    "pet",
    "pew",
    "phi",
    "pho",
    "pht",
    "pia",
    "pic",
    "pie",
    "pig",
    "pin",
    "pip",
    "pir",
    "pis",
    "pit",
    "piu",
    "pix",
    "ply",
    "pod",
    "poh",
    "poi",
    "pol",
    "pom",
    "poo",
    "pop",
    "pos",
    "pot",
    "pow",
    "pox",
    "pre",
    "pro",
    "pry",
    "psi",
    "pub",
    "pud",
    "pug",
    "pul",
    "pun",
    "pup",
    "pur",
    "pus",
    "put",
    "puy",
    "pya",
    "pye",
    "pyx",
    "qat",
    "qgp",
    "qis",
    "qua",
    "que",
    "qui",
    "quo",
    "rad",
    "rag",
    "rah",
    "rai",
    "raj",
    "ram",
    "ran",
    "rap",
    "ras",
    "rat",
    "rav",
    "raw",
    "rax",
    "ray",
    "rea",
    "reb",
    "rec",
    "red",
    "ree",
    "ref",
    "reg",
    "rem",
    "reo",
    "rep",
    "res",
    "ret",
    "rev",
    "rex",
    "rho",
    "ria",
    "rib",
    "rid",
    "rif",
    "rig",
    "rim",
    "rin",
    "rip",
    "rob",
    "roc",
    "rod",
    "roe",
    "rom",
    "roo",
    "rot",
    "row",
    "rub",
    "rue",
    "rug",
    "rum",
    "run",
    "rus",
    "rut",
    "rya",
    "rye",
    "ryu",
    "sab",
    "sac",
    "sad",
    "sae",
    "sag",
    "sai",
    "sal",
    "san",
    "sap",
    "sat",
    "sau",
    "saw",
    "sax",
    "say",
    "saz",
    "sea",
    "sec",
    "see",
    "sei",
    "sel",
    "sen",
    "seq",
    "ser",
    "ses",
    "set",
    "sev",
    "sew",
    "sex",
    "sez",
    "sha",
    "she",
    "shh",
    "shi",
    "sho",
    "shy",
    "sib",
    "sic",
    "sim",
    "sin",
    "sip",
    "sir",
    "sis",
    "sit",
    "six",
    "ska",
    "ski",
    "sky",
    "sly",
    "sob",
    "soc",
    "sod",
    "soh",
    "sol",
    "som",
    "son",
    "sop",
    "sos",
    "sot",
    "sou",
    "sow",
    "sox",
    "soy",
    "soz",
    "spa",
    "spy",
    "sri",
    "sty",
    "sub",
    "sue",
    "suh",
    "sui",
    "suk",
    "sum",
    "sun",
    "sup",
    "suq",
    "sus",
    "swy",
    "syn",
    "tab",
    "tad",
    "tae",
    "tag",
    "tai",
    "taj",
    "tal",
    "tam",
    "tan",
    "tao",
    "tap",
    "tar",
    "tas",
    "tat",
    "tau",
    "tav",
    "taw",
    "tax",
    "tch",
    "tea",
    "ted",
    "tee",
    "teg",
    "tej",
    "tel",
    "tem",
    "ten",
    "tet",
    "tew",
    "tfw",
    "the",
    "tho",
    "thy",
    "tic",
    "tie",
    "tig",
    "til",
    "tin",
    "tip",
    "tis",
    "tit",
    "tiz",
    "tod",
    "toe",
    "tog",
    "tom",
    "ton",
    "too",
    "top",
    "tor",
    "tot",
    "tow",
    "toy",
    "tra",
    "try",
    "tsk",
    "tub",
    "tug",
    "tui",
    "tum",
    "tun",
    "tup",
    "tur",
    "tut",
    "tux",
    "twa",
    "two",
    "tye",
    "uan",
    "udo",
    "ugh",
    "uke",
    "ult",
    "ulu",
    "umm",
    "ump",
    "umu",
    "und",
    "uni",
    "uns",
    "upo",
    "ups",
    "urb",
    "urd",
    "urn",
    "use",
    "uta",
    "ute",
    "uts",
    "vac",
    "van",
    "var",
    "vas",
    "vat",
    "vau",
    "vav",
    "vaw",
    "vee",
    "veg",
    "vet",
    "vex",
    "vey",
    "via",
    "vid",
    "vie",
    "vig",
    "vim",
    "vin",
    "vip",
    "vis",
    "voe",
    "vog",
    "von",
    "vow",
    "vox",
    "vug",
    "wab",
    "wad",
    "wae",
    "wag",
    "wah",
    "wan",
    "wap",
    "war",
    "was",
    "wat",
    "waw",
    "wax",
    "way",
    "waz",
    "web",
    "wed",
    "wee",
    "wei",
    "wen",
    "wet",
    "wey",
    "wha",
    "who",
    "why",
    "wig",
    "win",
    "wis",
    "wit",
    "wiz",
    "woe",
    "wok",
    "won",
    "woo",
    "wos",
    "wot",
    "wow",
    "wry",
    "wud",
    "wuz",
    "wye",
    "wyn",
    "xes",
    "xis",
    "yag",
    "yah",
    "yak",
    "yam",
    "yap",
    "yar",
    "yas",
    "yaw",
    "yay",
    "yea",
    "yeh",
    "yen",
    "yep",
    "yer",
    "yes",
    "yet",
    "yew",
    "yez",
    "yin",
    "yip",
    "yiz",
    "yob",
    "yod",
    "yok",
    "yom",
    "yon",
    "you",
    "yow",
    "yuk",
    "yum",
    "yup",
    "yus",
    "zac",
    "zag",
    "zap",
    "zas",
    "zax",
    "zed",
    "zee",
    "zek",
    "zen",
    "zes",
    "zho",
    "zig",
    "zin",
    "zip",
    "zit",
    "zoa",
    "zol",
    "zoo"
]
