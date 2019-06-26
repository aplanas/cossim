import argparse
import itertools
import os
import os.path

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def main(good, bad, sample):
    good = [os.path.join(good, f) for f in os.listdir(good)
            if os.path.isfile(os.path.join(good, f))]
    bad = [os.path.join(bad, f) for f in os.listdir(bad)
           if os.path.isfile(os.path.join(bad, f))]

    tfidf_good = TfidfVectorizer().fit_transform(
        [open(f, errors='ignore').read()
         for f in itertools.chain(good, [sample])])

    tfidf_bad = TfidfVectorizer().fit_transform(
        [open(f, errors='ignore').read()
         for f in itertools.chain(bad, [sample])])

    sim_good = cosine_similarity(tfidf_good[-1], tfidf_good)
    sim_bad = cosine_similarity(tfidf_bad[-1], tfidf_bad)

    index_good = sim_good.argsort()[0][-2]
    index_bad = sim_bad.argsort()[0][-2]

    print('Maximum similarity with good samples: {}', sim_good[0][index_good])
    print('Maximum similarity with bad samples: {}', sim_bad[0][index_bad])
    print('Similar document: {}'.format(
        good[index_good]
        if sim_good[0][index_good] >= sim_bad[0][index_bad]
        else bad[index_bad]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Basic cosine similarity comparator.')
    parser.add_argument('--good', help='directory were the good samples are')
    parser.add_argument('--bad', help='directory were the bad samples are')
    parser.add_argument('sample', help='file with to compare with')

    args = parser.parse_args()

    if not args.good or not args.bad:
        print('Provide directory path for good and bad samples')
        exit(1)

    main(args.good, args.bad, args.sample)
