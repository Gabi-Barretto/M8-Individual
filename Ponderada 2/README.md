## Robotic Simulation with ROS 2 and Webots

### 1. Introdução ao Projeto
Este projeto visa criar um pacote ROS 2 chamado "meu_pacote", que permite o controle de um robô simulado no ambiente Webots através da publicação e subscrição de coordenadas. Usando scripts Python para publicar (`pub.py`) e subscrever (`subs.py`) mensagens `PoseStamped`, o sistema será capaz de mover o robô de forma autônoma no ambiente simulado.

### 2. Requisitos do Sistema
Antes de prosseguir com a instalação e configuração do ROS 2 e Webots, certifique-se de que seu sistema atenda aos seguintes requisitos:

- **Sistema Operacional**: Ubuntu 20.04 LTS (ou compatível com a distribuição ROS 2 que você planeja usar).
- **Memória**: Mínimo de 4GB RAM (8GB recomendado).
- **Espaço em Disco**: Mínimo de 10GB de espaço livre.
- **Processador**: Mínimo de 2 núcleos (4 núcleos recomendado).
- **Gráficos**: GPU com suporte a OpenGL (para o Webots).

### 3. Instalação do ROS 2
A instalação do ROS 2 deve ser feita seguindo os passos abaixo:

1. **Instale o ROS 2 Foxy Fitzroy:**
   ```sh
   sudo apt update
   sudo apt install ros-humble-desktop
   ```

2. **Ambiente de Desenvolvimento:**
   - **Instale as dependências para a construção de pacotes:**
     ```sh
     sudo apt install python3-rosdep python3-colcon-common-extensions python3-flake8 python3-pytest-cov python3-ros-testing
     ```
   - **Inicialize o rosdep:**
     ```sh
     sudo rosdep init
     rosdep update
     ```

### 4. Configuração do Ambiente de Trabalho ROS 2
Criar e configurar um ambiente de trabalho ROS 2 é um processo essencial para o desenvolvimento de pacotes ROS. Aqui estão os passos para criar seu workspace:

```sh
mkdir -p ~/meu_workspace/src
cd ~/meu_workspace
colcon build
source ~/meu_workspace/install/setup.bash
```
Aqui infelizmente o Ubuntu resolveu nao colaborar mas os passos dos tutoriais foram seguidos meticulosamente. Ele funcionou o colcon build e o source foi ao arquivo zhs certo porem o ros não identificava o pacote.

### 5. Instalação do Webots
O Webots é um simulador de robôs de código aberto que será usado para simular o robô controlado por "meu_pacote". Siga as instruções oficiais para instalar o Webots no seu sistema.

### 6. Criação do Pacote ROS 2
Você já forneceu os arquivos de configuração do pacote (`package.xml` e `setup.py`). Para criar e construir o pacote dentro do workspace, você deve copiar os arquivos para o diretório `src` do seu workspace e executar `colcon build`.

### 7. Escrita dos Scripts Python
Os scripts fornecidos (`pub.py` e `subs.py`) já estão prontos para serem utilizados. Eles precisarão ser incluídos no seu pacote ROS 2 no diretório apropriado.

### 8. Configuração do Simple Commander para o Webots
Você precisará configurar o `nav2_simple_commander` para enviar comandos ao robô no Webots. Este é um passo que envolverá a integração do pacote `nav2_simple_commander` com o Webots e a configuração da pose inicial do robô.

### 9. Execução e Teste do Projeto
Após a configuração do ambiente e a construção do pacote, você pode executar os nós ROS 2 utilizando os comandos `ros2 run`.

### 10. Solução de Problemas Comuns
Todas as ferramentas utilizadas estão depreciadas, então são esperados diversos bugs e inacessibilidade por conta do ux das ferramentas, espere ter muitos problemas ao desenvolver com elas. 

### 11. Conclusão e Trabalhos Futuros
O mini projeto foi capaz de englobar os dois scripts essênciais para locomover o robô via um launcher das coordenadas a outro script que calcula sua movimentação e publica essas ao robô.
