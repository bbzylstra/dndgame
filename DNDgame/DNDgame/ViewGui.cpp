#include "game.h"
XY drawGui(XY mainGUI){
	sf::Vector2f viewPos;
	viewPos=mainGUI.view.getCenter();
	if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left)){
		mainGUI.view.setCenter(sf::Vector2f(viewPos.x-1,viewPos.y));
		viewPos=mainGUI.view.getCenter();
	}
	if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right)){
		mainGUI.view.setCenter(sf::Vector2f(viewPos.x+1,viewPos.y));
		viewPos=mainGUI.view.getCenter();
	}
	if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up)){
		mainGUI.view.setCenter(sf::Vector2f(viewPos.x,viewPos.y-1));
		viewPos=mainGUI.view.getCenter();
	}
	if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down)){
		mainGUI.view.setCenter(sf::Vector2f(viewPos.x,viewPos.y+1));
		viewPos=mainGUI.view.getCenter();
	}

		return mainGUI;
}