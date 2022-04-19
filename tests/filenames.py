import pytest

fnames = [
    pytest.param(
        " X-Men-V1-067.cbr",
        "hyphen separated with hyphen in series",
        {
            "issue": "67",
            "series": "X-Men",
            "title": "",
            "volume": "1",
            "year": "",
            "remainder": "",
            "issue_count": "",
        },
        marks=pytest.mark.xfail,
    ),
    (
        "Amazing Spider-Man 078.BEY (2022) (Digital) (Zone-Empire).cbr",
        "number issue with extra",
        {
            "issue": "78.BEY",
            "series": "Amazing Spider-Man",
            "volume": "",
            "year": "2022",
            "remainder": "(Digital) (Zone-Empire)",
            "issue_count": "",
        },
    ),
    pytest.param(
        "Angel Wings 02 - Black Widow (2015) (Scanlation) (phillywilly).cbr",
        "title after-issue",
        {
            "issue": "2",
            "series": "Angel Wings",
            "title": "Black Widow",
            "volume": "",
            "year": "2015",
            "remainder": "(Scanlation) (phillywilly)",
            "issue_count": "",
        },
        marks=pytest.mark.xfail,
    ),
    pytest.param(
        "Angel Wings #02 - Black Widow (2015) (Scanlation) (phillywilly).cbr",
        "title after-#issue",
        {
            "issue": "2",
            "series": "Angel Wings",
            "title": "Black Widow",
            "volume": "",
            "year": "2015",
            "remainder": "(Scanlation) (phillywilly)",
            "issue_count": "",
        },
        marks=pytest.mark.xfail,
    ),
    pytest.param(
        "Aquaman - Green Arrow - Deep Target 01 (of 07) (2021) (digital) (Son of Ultron-Empire).cbr",
        "issue count",
        {
            "issue": "1",
            "series": "Aquaman - Green Arrow - Deep Target",
            "volume": "",
            "year": "2021",
            "issue_count": "7",
            "remainder": "(digital) (Son of Ultron-Empire)",
        },
        marks=pytest.mark.xfail,
    ),
    (
        "Aquaman 80th Anniversary 100-Page Super Spectacular (2021) 001 (2021) (Digital) (BlackManta-Empire).cbz",
        "numbers in series",
        {
            "issue": "1",
            "series": "Aquaman 80th Anniversary 100-Page Super Spectacular",
            "volume": "2021",
            "year": "2021",
            "remainder": "(Digital) (BlackManta-Empire)",
            "issue_count": "",
        },
    ),
    pytest.param(
        "Avatar - The Last Airbender - The Legend of Korra (FCBD 2021) (Digital) (mv-DCP).cbr",
        "FCBD date",
        {
            "issue": "",
            "series": "Avatar - The Last Airbender - The Legend of Korra",
            "volume": "",
            "year": "2021",
            "remainder": "(FCBD) (Digital) (mv-DCP)",
            "issue_count": "",
        },
        marks=pytest.mark.xfail,
    ),
    pytest.param(
        "Avengers By Brian Michael Bendis v03 (2013) (Digital) (F2) (Kileko-Empire).cbz",
        "volume without issue",
        {
            "issue": "",
            "series": "Avengers By Brian Michael Bendis",
            "volume": "3",
            "year": "2013",
            "remainder": "(Digital) (F2) (Kileko-Empire)",
            "issue_count": "",
        },
        marks=pytest.mark.xfail,
    ),
    (
        "Batman '89 (2021) (Webrip) (The Last Kryptonian-DCP).cbr",
        "year in title without issue",
        {
            "issue": "",
            "series": "Batman '89",
            "volume": "",
            "year": "2021",
            "remainder": "(Webrip) (The Last Kryptonian-DCP)",
            "issue_count": "",
        },
    ),
    (
        "Batman_-_Superman_020_(2021)_(digital)_(NeverAngel-Empire).cbr",
        "underscores",
        {
            "issue": "20",
            "series": "Batman - Superman",
            "volume": "",
            "year": "2021",
            "remainder": "(digital) (NeverAngel-Empire)",
            "issue_count": "",
        },
    ),
    (
        "Black Widow 009 (2021) (Digital) (Zone-Empire).cbr",
        "standard",
        {
            "issue": "9",
            "series": "Black Widow",
            "volume": "",
            "year": "2021",
            "remainder": "(Digital) (Zone-Empire)",
            "issue_count": "",
        },
    ),
    (
        "Blade Runner 2029 006 (2021) (3 covers) (digital) (Son of Ultron-Empire).cbr",
        "year before issue",
        {
            "issue": "6",
            "series": "Blade Runner 2029",
            "volume": "",
            "year": "2021",
            "remainder": "(3 covers) (digital) (Son of Ultron-Empire)",
            "issue_count": "",
        },
    ),
    pytest.param(
        "Blade Runner Free Comic Book Day 2021 (2021) (digital-Empire).cbr",
        "FCBD year and (year)",
        {
            "issue": "",
            "series": "Blade Runner Free Comic Book Day 2021",
            "volume": "",
            "year": "2021",
            "remainder": "(digital-Empire)",
            "issue_count": "",
        },
        marks=pytest.mark.xfail,
    ),
    pytest.param(
        "Bloodshot Book 03 (2020) (digital) (Son of Ultron-Empire).cbr",
        "book",
        {
            "issue": "3",
            "series": "Bloodshot",
            "title": "Book 03",
            "volume": "3",
            "year": "2020",
            "remainder": "(digital) (Son of Ultron-Empire)",
            "issue_count": "",
        },
        marks=pytest.mark.xfail,
    ),
    pytest.param(
        "Cyberpunk 2077 - You Have My Word 02 (2021) (digital) (Son of Ultron-Empire).cbr",
        "title",
        {
            "issue": "2",
            "series": "Cyberpunk 2077",
            "title": "You Have My Word",
            "volume": "",
            "year": "2021",
            "issue_count": "",
            "remainder": "(digital) (Son of Ultron-Empire)",
        },
        marks=pytest.mark.xfail,
    ),
    pytest.param(
        "Elephantmen 2259 008 - Simple Truth 03 (of 06) (2021) (digital) (Son of Ultron-Empire).cbr",
        "volume count",
        {
            "issue": "8",
            "series": "Elephantmen 2259",
            "title": "Simple Truth",
            "volume": "3",
            "year": "2021",
            "volume_count": "6",
            "remainder": "(digital) (Son of Ultron-Empire)",
            "issue_count": "",
        },
        marks=pytest.mark.xfail,
    ),
    pytest.param(
        "Elephantmen 2259 #008 - Simple Truth 03 (of 06) (2021) (digital) (Son of Ultron-Empire).cbr",
        "volume count",
        {
            "issue": "8",
            "series": "Elephantmen 2259",
            "title": "Simple Truth",
            "volume": "3",
            "year": "2021",
            "volume_count": "6",
            "remainder": "(digital) (Son of Ultron-Empire)",
            "issue_count": "",
        },
        marks=pytest.mark.xfail,
    ),
    pytest.param(
        "Free Comic Book Day - Avengers.Hulk (2021) (2048px) (db).cbz",
        "'.' in name",
        {
            "issue": "",
            "series": "Free Comic Book Day - Avengers Hulk",
            "volume": "",
            "year": "2021",
            "remainder": "(2048px) (db)",
            "issue_count": "",
        },
        marks=pytest.mark.xfail,
    ),
    (
        "Goblin (2021) (digital) (Son of Ultron-Empire).cbr",
        "no-issue",
        {
            "issue": "",
            "series": "Goblin",
            "volume": "",
            "year": "2021",
            "remainder": "(digital) (Son of Ultron-Empire)",
            "issue_count": "",
        },
    ),
    pytest.param(
        "Marvel Previews 002 (January 2022) (Digital-Empire).cbr",
        "(month year)",
        {
            "issue": "2",
            "series": "Marvel Previews",
            "volume": "",
            "year": "2022",
            "remainder": "(Digital-Empire)",
            "issue_count": "",
        },
        marks=pytest.mark.xfail,
    ),
    pytest.param(
        "Marvel Two In One V1 090  c2c (Comixbear-DCP).cbr",
        "volume issue ctc",
        {
            "issue": "90",
            "series": "Marvel Two In One",
            "volume": "1",
            "year": "",
            "remainder": "c2c (Comixbear-DCP)",
            "issue_count": "",
        },
        marks=pytest.mark.xfail,
    ),
    (
        "Marvel Two In One V1 #090  c2c (Comixbear-DCP).cbr",
        "volume then issue",
        {
            "issue": "90",
            "series": "Marvel Two In One",
            "volume": "1",
            "year": "",
            "remainder": "c2c (Comixbear-DCP)",
            "issue_count": "",
        },
    ),
    pytest.param(
        "Star Wars - War of the Bounty Hunters - IG-88 (2021) (Digital) (Kileko-Empire).cbz",
        "number ends series, no-issue",
        {
            "issue": "",
            "series": "Star Wars - War of the Bounty Hunters - IG-88",
            "volume": "",
            "year": "2021",
            "remainder": "(Digital) (Kileko-Empire)",
            "issue_count": "",
        },
        marks=pytest.mark.xfail,
    ),
    (
        "Star Wars - War of the Bounty Hunters - IG-88 #1 (2021) (Digital) (Kileko-Empire).cbz",
        "number ends series",
        {
            "issue": "1",
            "series": "Star Wars - War of the Bounty Hunters - IG-88",
            "volume": "",
            "year": "2021",
            "remainder": "(Digital) (Kileko-Empire)",
            "issue_count": "",
        },
    ),
    (
        "The Defenders v1 058 (1978) (digital).cbz",
        "",
        {
            "issue": "58",
            "series": "The Defenders",
            "volume": "1",
            "year": "1978",
            "remainder": "(digital)",
            "issue_count": "",
        },
    ),
    pytest.param(
        "The Defenders v1 Annual 01 (1976) (Digital) (Minutemen-Slayer).cbr",
        " v in series",
        {
            "issue": "1",
            "series": "The Defenders Annual",
            "volume": "1",
            "year": "1976",
            "remainder": "(Digital) (Minutemen-Slayer)",
            "issue_count": "",
        },
        marks=pytest.mark.xfail,
    ),
    pytest.param(
        "The Magic Order 2 06 (2022) (Digital) (Zone-Empire)[__913302__].cbz",
        "ending id",
        {
            "issue": "6",
            "series": "The Magic Order 2",
            "volume": "",
            "year": "2022",
            "remainder": "(Digital) (Zone-Empire)[__913302__]",
            "issue_count": "",
        },
        marks=pytest.mark.xfail,
    ),
    pytest.param(
        "Wonder Woman 001 Wonder Woman Day Special Edition (2021) (digital-Empire).cbr",
        "issue separates title",
        {
            "issue": "1",
            "series": "Wonder Woman",
            "title": "Wonder Woman Day Special Edition",
            "volume": "",
            "year": "2021",
            "remainder": "(digital-Empire)",
            "issue_count": "",
        },
        marks=pytest.mark.xfail,
    ),
    pytest.param(
        "Wonder Woman #001 Wonder Woman Day Special Edition (2021) (digital-Empire).cbr",
        "issue separates title",
        {
            "issue": "1",
            "series": "Wonder Woman",
            "title": "Wonder Woman Day Special Edition",
            "volume": "",
            "year": "2021",
            "remainder": "(digital-Empire)",
            "issue_count": "",
        },
        marks=pytest.mark.xfail,
    ),
    pytest.param(
        "Wonder Woman 49 DC Sep-Oct 1951 digital [downsized, lightened, 4 missing story pages restored] (Shadowcat-Empire).cbz",
        "date-range, no paren, braces",
        {
            "issue": "49",
            "series": "Wonder Woman",
            "volume": "",
            "year": "1951",
            "remainder": "(Shadowcat-Empire)",
            "issue_count": "",
        },
        marks=pytest.mark.xfail,
    ),
    pytest.param(
        "Wonder Woman #49 DC Sep-Oct 1951 digital [downsized, lightened, 4 missing story pages restored] (Shadowcat-Empire).cbz",
        "date-range, no paren, braces",
        {
            "issue": "49",
            "series": "Wonder Woman",
            "volume": "",
            "year": "1951",
            "remainder": "(Shadowcat-Empire)",
            "issue_count": "",
        },
        marks=pytest.mark.xfail,
    ),
    pytest.param(
        "X-Men, 2021-08-04 (#02) (digital) (Glorith-HD).cbz",
        "full-date, issue in parenthesis",
        {
            "issue": "2",
            "series": "X-Men",
            "volume": "",
            "year": "2021",
            "remainder": "(digital) (Glorith-HD)",
            "issue_count": "",
        },
        marks=pytest.mark.xfail,
    ),
]

rnames = [
    (
        "{series} #{issue} - {title} ({year})",
        False,
        "universal",
        "Cory Doctorow's Futuristic Tales of the Here and Now #001 - Anda's Game (2007).cbz",
    ),
    (
        "{series}: {title} #{issue} ({year})",
        False,
        "universal",
        "Cory Doctorow's Futuristic Tales of the Here and Now - Anda's Game #001 (2007).cbz",
    ),
    pytest.param(
        "{series}: {title} #{issue} ({year})",
        False,
        "Linux",
        "Cory Doctorow's Futuristic Tales of the Here and Now: Anda's Game #001 (2007).cbz",
        marks=pytest.mark.xfail,
    ),
    pytest.param(
        "{publisher}/  {series} #{issue} - {title} ({year})",
        True,
        "universal",
        "IDW Publishing/Cory Doctorow's Futuristic Tales of the Here and Now #001 - Anda's Game (2007).cbz",
        marks=pytest.mark.xfail,
    ),
    pytest.param(
        "{publisher}/  {series} #{issue} - {title} ({year})",
        False,
        "universal",
        "Cory Doctorow's Futuristic Tales of the Here and Now #001 - Anda's Game (2007).cbz",
        marks=pytest.mark.xfail,
    ),
    (
        "{series} #  {issue} - {title} ({year})",
        False,
        "universal",
        "Cory Doctorow's Futuristic Tales of the Here and Now # 001 - Anda's Game (2007).cbz",
    ),
    pytest.param(
        "{series} #  {issue} - {locations} ({year})",
        False,
        "universal",
        "Cory Doctorow's Futuristic Tales of the Here and Now # 001 - lonely cottage (2007).cbz",
        marks=pytest.mark.xfail,
    ),
    pytest.param(
        "{series} #{issue} - {title} - {WriteR}, {EDITOR} ({year})",
        False,
        "universal",
        "Cory Doctorow's Futuristic Tales of the Here and Now #001 - Anda's Game - Dara Naraghi, Ted Adams (2007).cbz",
        marks=pytest.mark.xfail,
    ),
]
