from deap import tools
import copy
import random


class Mutation(object):
    def __init__(self, individuals, prob_, _log):
        self.individuals = individuals
        self.prob = prob_
        self.log = _log

    def do_mutation(self):
        after_mut = []
        for indi_no in self.individuals:
            indi_tmp = copy.deepcopy(indi_no)
            if indi_tmp.acc > 0:
                p_ = random.random()
                if p_ < self.prob:
                    self.log.info("Mutation happen for %s" % (indi_tmp.id))
                    indi_tmp.indi = tools.mutShuffleIndexes(indi_no.indi, 0.05)[0]
                    indi_tmp.acc = -1
                    after_mut.append(indi_tmp)
                else:
                    self.log.info("Mutation do not happen for %s" % (indi_tmp.id))
            else:
                after_mut.append(indi_tmp)
        return after_mut


class Crossover(object):
    def __init__(self, individuals, prob_, _log):
        self.individuals = individuals
        self.prob = prob_
        self.log = _log

    def crossover(self):
        indis = []
        for i in range(1, len(self.individuals) // 2):
            idx1, idx2 = 2 * i - 2, 2 * i - 1
            parent1, parent2 = self.individuals[idx1], self.individuals[idx2]
            tmp1 = copy.deepcopy(parent1)
            tmp2 = copy.deepcopy(parent2)
            p_ = random.random()
            if p_ < self.prob:
                self.log.info("crossover happen between %s and %s" % (tmp1.id, tmp2.id))
                tmp1.indi, tmp2.indi = tools.cxOrdered(parent1.indi, parent2.indi)
                tmp1.acc = -1
                tmp2.acc = -1
            else:
                self.log.info("crossover do not happen between %s and %s" % (tmp1.id, tmp2.id))
            indis.append(tmp1)
            indis.append(tmp2)
        return indis
