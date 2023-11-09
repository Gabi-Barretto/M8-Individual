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

1. **Configure seu computador para aceitar software de packages.ros.org:**
   ```sh
   sudo apt update && sudo apt install curl gnupg2 lsb-release
   curl -s https://raw.githubusercontent.com/ros/rosdistro/master/ros.asc | sudo apt-key add -
   ```

2. **Adicione o repositório do ROS 2 ao seu sistema:**
   ```sh
   sudo sh -c 'echo "deb [arch=amd64,arm64] http://packages.ros.org/ros2/ubuntu `lsb_release -cs` main" > /etc/apt/sources.list.d/ros2-latest.list'
   ```

3. **Instale o ROS 2 Foxy Fitzroy:**
   ```sh
   sudo apt update
   sudo apt install ros-foxy-desktop
   ```

4. **Ambiente de Desenvolvimento:**
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
Inclua uma seção de solução de problemas comuns para ajudar os usuários a resolver problemas que possam surgir durante a configuração ou execução do pacote.

### 11. Conclusão e Trabalhos Futuros
Finalize com uma conclusão sobre o projeto e sugestões para desenvolvimentos futuros, como a adição de mais funcionalidades ou a integração com outros sistemas e sensores.

**Nota:** Esta é uma estrutura básica de documentação. Cada seção deve ser expandida com detalhes específicos, comandos precisos, e instruções passo a passo conforme necessário para o seu projeto específico.
