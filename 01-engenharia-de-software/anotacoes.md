# Engenharia de Software - Módulo 1

## Anotações da Aula: 1 - Introdução à Engenharia de Software: Ciclo de Vida, Processos e Modelos (Cascata, Iterativo, Ágil)
O que é Engenharia de Software?
* R. Engenharia de Softer é sobre disciplina, é Sobre tornar o desenvolvimento previsível, confiável mesmo com o sistema complexo.
     * Disciplina que organiza o desenvolvimento de sistemas
     * Define métodos, ferramentas e boas práticas;
     * Foca em qualidade, custo, prazo e manutenção.


Hoje aprendi sobre como os softwares seguem um cíclo, eles nascem, crescem e evoluem:

* **Classes:** O molde ou a planta do objeto.
* **Objetos:** A instância real da classe.

### Meu entendimento prático:
Na empresa onde trabalho, posso usar uma classe chamada `Usuario` para mapear os dados de login do sistema.

### Exemplo de código em Python que testei:
```python
class Desenvolvedor:
    def __init__(self, nome, nivel):
        self.nome = nome
        self.nivel = nivel

    def codificar(self):
        return f"{self.nome} está escrevendo código como {self.nivel}."

# Testando a classe
dev = Desenvolvedor("Raul", "Sênior")
print(dev.codificar())
```
----------------------------------
# Programação orientada a objetos (POO): Classes, Objetos, Encapsulamento, Herança w Polimorfismo

Descrição da aula

Nesta unidade, abordaremos os princípios fundamentais da Programação Orientada a Objetos (POO), um dos modelos mais consolidados no desenvolvimento de software moderno. Discutiremos os conceitos essenciais da POO, como Classes, Objetos, Encapsulamento, Herança e Polimorfismo, de forma clara, prática e contextualizada. Por fim, analisaremos como a POO melhora a modularidade, a manutenção e a extensibilidade de sistemas, mostrando exemplos didáticos aplicáveis a diversas linguagens, como Python, Java e C#.

# Competências adquiridas

 * Compreender os conceitos principais da Programação Orientada a Objetos.
 * Distinguir Classes e Objetos e entender sua relação na modelagem de sistemas.
 * Abordar princípios de Encapsulamento para proteger e organizar dados.
 * Interpretar e implementar Herança em estruturas de código.
 * Visualizar a aplicação prática da POO em problemas reais.

----------------------------------

# Princípios de Design de Código: SOLID, Clean Code e Boas Práticas de Codificação

## Descrição da aula

Nesta unidade, abordaremos princípios de design de código utilizados no desenvolvimento de software profissional, com foco em SOLID, Clean Code e boas práticas de codificação. Para tanto, estudaremos os conceitos fundamentais que auxiliam na redução de erros, na facilitação da manutenção e na melhoria da colaboração em equipes de desenvolvimento. Discutiremos ainda princípios amplamente adotados pela indústria de software e aplicáveis a diversas linguagens de programação, como Java, Python, C#, JavaScript e outras.

## Competências adquiridas

   * Compreender a importância do design de código na qualidade de software.
   * Identificar problemas comuns causados por código mal estruturado.
   * Aplicar os cinco princípios SOLID na organização de classes e módulos.
   * Discutir as características de um código limpo (Clean Code).
   * Abordar as boas práticas de codificação para melhorar legibilidade e manutenção.

---

# Estruturas de Dados e Algoritmos Essenciais para Engenheiros de Software

## Descrição da aula

Nesta unidade, estudaremos os principais conceitos de estruturas de dados e algoritmos, fundamentais para a formação de engenheiros de software e discutiremos como os dados são organizados, armazenados e manipulados de forma eficiente, impactando diretamente o desempenho, a escalabilidade e a qualidade dos sistemas. Abordaremos ainda estruturas clássicas, como listas, pilhas, filas, árvores e grafos, além de algoritmos básicos de busca e ordenação, sempre com foco conceitual e aplicação prática no desenvolvimento de software.

## Competências adquiridas

   * Compreender a importância das estruturas de dados no desempenho dos sistemas.
   * Identificar as principais estruturas de dados utilizadas.
   * Diferenciar estruturas lineares e não lineares.
   * Reconhecer quando utilizar cada estrutura de dados em diferentes contextos.
   * Abordar o papel dos algoritmos de busca e ordenação.

---

