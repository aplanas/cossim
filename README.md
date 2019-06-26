# cossim
PoC for text similarity using the cosine distance

## Setup

```bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

There are two samples that I take from the samples (`good` and `bad`):

```bash
diff -u ./good/000021f5c87d56000fd13a651be10b19.txt sample_from_good.txt
diff -u ./bad/000007e9c8f71febdfb37b51b6bbed77.txt sample_from_bad.txt
```

The changed documents are properly identified:

```bash
python3 cossim.py --good ./good --bad ./bad sample_from_bad.txt

Maximum similarity with good samples: {} 0.2326964857509056
Maximum similarity with bad samples: {} 0.9995798580507443
Similar document: ./bad/000007e9c8f71febdfb37b51b6bbed77.txt
```

```bash
python3 cossim.py --good ./good --bad ./bad sample_from_good.txt

Maximum similarity with good samples: {} 0.9960348410695655
Maximum similarity with bad samples: {} 0.3742297492165573
Similar document: ./good/000021f5c87d56000fd13a651be10b19.txt
```

