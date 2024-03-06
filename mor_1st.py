def fun(n, state):
    ant_state = list(map(str, state))
    ant_bite = [0] * n
    ant_value = []
    for i in range(n):
        ant_value.append(float(i))

    print(ant_state, ant_value, ant_bite)
    ant_step = 0.5

    for i in range(n):
        for j in range(n):
            ant_value[j] += -ant_step if ant_state[j] == 'L' else ant_step
        for k in range(n - 1):
            if ant_value[k] == ant_value[k + 1]:
                for l in [k, k + 1]:
                    ant_state[l] = 'P' if ant_state[l] == 'L' else 'L'
                    ant_bite[l] += 1

        print(ant_state, ant_value, ant_bite)


if __name__ == '__main__':
    fun(6, 'LPPLPL')
