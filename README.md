# Four-Corners-Showdown

This repository contains a multiplayer game developed using Python, utilizing `pygame` for graphics and `socket` for client-server communication. The game supports four players and features a puck and player mechanics for an exciting interactive experience.

---

## Features
- **Multiplayer Support:** Up to 4 players can join a game.
- **Real-Time Gameplay:** Players interact with each other in real time via a server-client architecture.
- **Smooth Animations:** Built using `pygame` for seamless visuals and gameplay.
- **Secure Communication:** Uses SSL (optional) for encrypted connections.

---

## Prerequisites

1. Python 3.7+
2. `pygame` library:
   ```bash
   pip install pygame
   ```
3. SSL Certificates (optional for secure connections):
   - `server.crt` (certificate file)
   - `server.key` (private key file)

---

## File Structure

- `server.py`: The server code managing connections, games, and player actions.
- `client.py`: The client code for connecting to the server and rendering the game.
- `game.py`: Contains game logic and class definitions for players, puck, and the game.
- `network.py`: Handles network communication between client and server.
- `variables.py`: Stores constants like colors and velocity values.

---

## How to Run

### Step 1: Start the Server
1. Open a terminal and navigate to the project directory.
2. Run the server:
   ```bash
   python server.py
   ```
3. The server will start listening on `localhost:5555`.

### Step 2: Start the Clients
1. Open a new terminal for each client.
2. Run the client:
   ```bash
   python client.py
   ```
3. The game window will open, and the client will connect to the server.
4. Repeat for up to 4 players.

---

## Gameplay Instructions

1. Use arrow keys to move your player.
2. The objective is to avoid letting the puck reach your corner.
3. If the puck enters a corner, that player loses.
4. The game resets automatically after determining the winner.

---

## SSL Configuration (Optional)

To enable secure communication:
1. Uncomment the SSL-related lines in `server.py`.
2. Place `server.crt` and `server.key` in the project directory.
3. Modify the `Network` class in `network.py` to use an SSL-wrapped socket.

---

## Suggested Improvements

### General Enhancements
- **Add a Main Menu:** Provide options for players to choose teams, colors, or other preferences.
- **Leaderboard:** Implement a scoring system and display player rankings.
- **Dynamic Port Configuration:** Allow the server and client to specify the port via command-line arguments.

### Gameplay Improvements
- **Power-Ups:** Introduce special items (e.g., speed boost, shield).
- **Advanced Physics:** Improve puck movement and collision mechanics.
- **Customizable Settings:** Allow players to customize game speed, puck size, etc.

### Technical Enhancements
- **Error Handling:** Add robust error handling for disconnections and invalid data.
- **Unit Tests:** Write tests for critical game functionalities (e.g., collision detection).
- **Scalability:** Modify the server to support multiple simultaneous games.

---

## Known Issues
- **Collision Glitches:** Occasionally, collisions between the puck and players may not behave as expected.
- **Connection Drops:** Clients may disconnect if the server fails to handle unexpected errors.

---

## Authors
- **Yuvaneshwarran R**

---

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

---

Enjoy the game!
