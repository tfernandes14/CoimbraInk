import csv

with open('Reprografias.csv', encoding='utf8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    id = 1
    valores = []

    array_insert = []
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            valores.clear()
            for k in range(16):
                valores.append(row[k])
            #print(len(valores))
            valores.append(row[58])
           # print(len(valores))
            string = 'INSERT INTO public.website_reprografia(id, nome, zona, latitude, longitude, webiste, contacto, email, rating_medio, horario_abertura_semana_manha, horario_fecho_semana_manha, horario_abertura_semana_tarde, horario_fecho_semana_tarde, horario_abertura_fds_manha, horario_fecho_fds_manha, horario_abertura_fds_tarde, horario_fecho_fds_tarde, cartao_visita_preco) VALUES ({},"{}","{}",{},{},"{}",{},"{}",{},{},{},{},{},{},{},{},{},{});'.format(id,valores[0], valores[1], valores[2], valores[3], valores[4], valores[5], valores[6],valores[7], valores[8], valores[9], valores[10], valores[11], valores[12], valores[13], valores[14], valores[15], valores[16])

            valores.clear()
            array_insert.append(string)

            for l in range(7):
                valores.append(row[16+l])

            string2 = 'INSERT INTO public.website_acinco(reprografia_id, frente_cor_preco, frente_preto_branco_preco, frente_verso_cor_preco, frente_verso_preto_branco_preco, encadernacao, digitalizacao, plastificacao) VALUES ({},{},{},{},{},{},{},{});'.format(id,valores[0],valores[1],valores[2],valores[3],valores[4],valores[5],valores[6])
            array_insert.append(string2)
            valores.clear()

            for l in range(7):
                valores.append(row[23+l])

            string3 = 'INSERT INTO public.website_aquatro(reprografia_id, frente_cor_preco, frente_preto_branco_preco, frente_verso_cor_preco, frente_verso_preto_branco_preco, encadernacao, digitalizacao, plastificacao) VALUES ({},{},{},{},{},{},{},{});'.format(id,valores[0],valores[1],valores[2],valores[3],valores[4],valores[5],valores[6])
            array_insert.append(string3)

            valores.clear()

            for l in range(7):
                valores.append(row[30+l])

            string4 = 'INSERT INTO public.website_atres(reprografia_id, frente_cor_preco, frente_preto_branco_preco, frente_verso_cor_preco, frente_verso_preto_branco_preco, encadernacao, digitalizacao, plastificacao) VALUES ({},{},{},{},{},{},{},{});'.format(id,valores[0],valores[1],valores[2],valores[3],valores[4],valores[5],valores[6])
            array_insert.append(string4)

            valores.clear()
            for l in range(7):
                valores.append(row[37+l])

            string5 = 'INSERT INTO public.website_adois(reprografia_id, frente_cor_preco, frente_preto_branco_preco, frente_verso_cor_preco, frente_verso_preto_branco_preco, encadernacao, digitalizacao, plastificacao) VALUES ({},{},{},{},{},{},{},{});'.format(id,valores[0],valores[1],valores[2],valores[3],valores[4],valores[5],valores[6])
            array_insert.append(string5)

            valores.clear()
            for l in range(7):
                valores.append(row[44+l])

            string6 = 'INSERT INTO public.website_aum(reprografia_id, frente_cor_preco, frente_preto_branco_preco, frente_verso_cor_preco, frente_verso_preto_branco_preco, encadernacao, digitalizacao, plastificacao) VALUES ({},{},{},{},{},{},{},{});'.format(id,valores[0],valores[1],valores[2],valores[3],valores[4],valores[5],valores[6])
            array_insert.append(string6)

            valores.clear()

            for l in range(7):
                valores.append(row[51+l])

            string7 = 'INSERT INTO public.website_azero(reprografia_id, frente_cor_preco, frente_preto_branco_preco, frente_verso_cor_preco, frente_verso_preto_branco_preco, encadernacao, digitalizacao, plastificacao) VALUES ({},{},{},{},{},{},{},{});'.format(id,valores[0],valores[1],valores[2],valores[3],valores[4],valores[5],valores[6])
            array_insert.append(string7)

            valores.clear()
            line_count += 1
            id += 1

    with open("inserts.txt", 'w', encoding="utf8") as output:
        for k in range(len(array_insert)):
            output.write(array_insert[k] + '\n')
