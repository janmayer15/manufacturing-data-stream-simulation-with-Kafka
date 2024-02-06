# Manufacturing Data Stream Simulation with Kafka

This GitHub project provides a comprehensive setup for simulating real-time manufacturing data streams using Apache Kafka. It is designed to help developers explore and experiment with industrial stream processing for various applications. This README will guide you through the setup and usage of the project.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Simulation](#running-the-simulation)
- [Reading the Latest Message](#reading-the-latest-message)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before you can start using this project, ensure that you have the following prerequisites installed on your system:

1. [Docker](https://www.docker.com/products/docker-desktop/): This project utilizes Docker for containerization, making it easy to set up and run the required components.

## Installation

Follow these steps to set up and run the manufacturing data stream simulation:

1. **Download Docker**: If you haven't already, visit the [Docker website](https://www.docker.com/products/docker-desktop/) and download Docker Desktop for your operating system. Docker will be used to containerize the required services.

2. **Clone the Repository**: Clone this GitHub repository to your local machine using the following command:

   ```bash
   git clone https://github.com/janmayer15/manufacturing-data-stream-simulation-with-Kafka.git
   ```

3. **Install Requirements**: Navigate to the `/src` directory of the cloned repository and install the Python dependencies using pip. You can do this by running the following command:

   ```bash
   cd manufacturing-data-stream-simulation-with-Kafka/src
   pip install -r requirements.txt
   ```

## Running the Simulation

Now that you have successfully set up the prerequisites and installed the required dependencies, you can run the manufacturing data stream simulation:

1. **Start Docker Services**: From the root directory of the cloned repository, run the following command to start the Docker services defined in the `docker-compose.yml` file:

   ```bash
   docker-compose up
   ```

2. **Create Kafka Topic**: After the Docker services are up and running, create a new Kafka topic named "manufacturing_data_stream" using the Kafka command-line tools or a Kafka management tool of your choice. To create the necessary Kafka topic for the manufacturing data stream simulation, follow these steps:

#### 2.1 Access the Control Center on localhost:9021

Open your web browser and navigate to `http://localhost:9021` to access the Kafka Control Center.

#### 2.2 Click on "Control Center Cluster"

In the Kafka Control Center, locate and click on the "Control Center Cluster" option in the left navigation menu.

![Screen_Topics](/images/Screen_Topics.png)

#### 2.3 Click on Topics

After selecting "Control Center Cluster," you will see a list of available options. Click on "Topics" to manage Kafka topics.

#### 2.4 Click on Add Topic

Within the Topics section, click on the "Add Topic" button to create a new topic for the manufacturing data stream simulation.

![Screen_Add_Topic](/images/Screen_Add_Topic.png)

#### 2.5 Enter the Name of the Topic

A pop-up window will appear for configuring the new topic. Follow these steps:

- Enter the name of the topic as "manufacturing_data_stream" in the "Name" field.

![Screen_Topic_Name](/images/Screen_Topic_Name.png)

- Click on "Create with defaults" to create the topic with default settings. This ensures that the topic is created with the necessary configurations for the manufacturing data stream simulation.

Now, you have successfully set up the required Kafka topic for the manufacturing data stream simulation. The producer will publish data to this topic, and you can proceed with running the simulation as described in the previous steps.

3. **Start the Producer**: In the `/src` directory, open a Python prompt and run the `producer.py` script to start simulating manufacturing data streams. Use the following command:

   ```bash
   python producer.py
   ```

4. **Simulating Data**: The producer script will begin sending simulated manufacturing data to the Kafka topic you created earlier.

## Reading the Latest Message

To read the latest message from the manufacturing data stream, you can use the provided `read_latest_message.py` script. Here's how:

1. In the `/src` directory, open a Python prompt.

2. Run the `read_latest_message.py` or `consumer.py` script:

   ```bash
   python read_latest_message.py
   ```

   ```bash
   consumer.py
   ```
   
This script will retrieve and display the most recent message from the "manufacturing_data_stream" Kafka topic.

## Contributing

Contributions to this project are welcome. Feel free to open issues, create pull requests, or suggest improvements. Please follow the project's code of conduct and contribution guidelines.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute it as needed.
