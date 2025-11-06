# 🎮✨ A Jornada do Herói - RPG em Python POO

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Status](https://img.shields.io/badge/status-concluído-success)
![Score](https://img.shields.io/badge/pontuação-450%2F450-brightgreen)

> ⚔️ Um RPG desenvolvido em Python aplicando todos os conceitos de **Programação Orientada a Objetos (POO)**, onde cada etapa do desafio adiciona novas funcionalidades ao jogo. 🛡️

---

## 📋 Sobre o Projeto

Este projeto é uma **atividade didática de RPG**, estruturada em **30 questões**, cada uma adicionando uma funcionalidade ao jogo.  

🎯 **Objetivos principais:**
- Aprender e aplicar conceitos de **POO** de forma prática e divertida.  
- Criar heróis, inimigos, armas, poções e sistema de combate.  
- Demonstrar a evolução do código e do jogo passo a passo.  

---

## 🧩 Personagens Jogáveis

✨ **Heróis:**
- **Guerreiro ⚔️**: especialista em combate corpo a corpo.  
- **Mago ✨**: usa magia e habilidades especiais.  
- **Arqueiro 🏹**: ataque à distância com alta precisão.  

👹 **Inimigos:**
- Goblins, Orcs e outros monstros, cada um com atributos próprios (vida, ataque e habilidades especiais).  

🛡️ **Itens:**
- Armas 🗡️ para aumentar o ataque.  
- Poções 🍷 para recuperar vida.  

⚔️ **Sistema de Ataque:**
- Ataque básico: personagem causa dano ao inimigo.  
- Ataque real: ataque base + arma equipada.  

---

## 🧠 Conceitos de POO Aplicados

- **📝 Classes e Objetos:** criação de heróis, inimigos e itens.  
- **🔒 Encapsulamento:** proteção de atributos críticos (como vida).  
- **📜 Herança:** classes derivadas de `Personagem`.  
- **🔄 Polimorfismo:** métodos de ataque e habilidades únicos para cada classe.  
- **🧩 Composição:** personagens possuem armas, poções e inventário.  
- **📦 Abstração:** habilidades e ataques seguem contratos definidos por classes base.  

---

## 🔥 Evolução do Jogo

### **Nível Básico (1-10) – O Despertar do Herói**
- Criação de heróis: Guerreiro, Mago e Arqueiro  
- Criação de inimigos básicos: Goblins  
- Visualização do status de cada personagem  
- Ataque simples entre heróis e monstros  
- Criação de armas e poções  
- Equipamento de armas e ataque real  

### **Nível Intermediário (11-20) – A Forja das Lendas**
- Evita repetição criando classe base `Personagem`  
- Proteção do atributo vida com `@property` e `@setter`  
- Método `receber_dano()` para dano realista  
- Ataques com efeito concreto nos inimigos  
- Inventário para armazenar armas e poções  
- Uso de poções para recuperação de vida  
- Ataques únicos para cada classe (magia, precisão, força)  
- Fábrica de monstros para criar Goblins padrão  
- Método `esta_vivo()` para controlar sobrevivência  

### **Nível Avançado (21-30) – O Panteão dos Campeões**
- Criação de molde de habilidades (`Habilidade`)  
- Habilidades concretas: AtaqueForte e BolaDeFogo  
- Personagem pode usar qualquer habilidade contra inimigos  
- Aleatoriedade no dano usando a classe `Dado`  
- Combate imprevisível: dano variável com dados  
- Inimigos mais fortes: Orcs com ataques críticos  
- Gerenciador de batalhas centraliza regras de combate  
- Sistema de turnos para combate estratégico  
- Determinação do vencedor da batalha  
- Batalhas em equipe entre grupos de heróis e inimigos  

---






