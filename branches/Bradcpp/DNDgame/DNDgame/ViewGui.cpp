#include "game.h"
XY drawGui(XY mainGUI){
	sf::Vector2f viewPos;
	sf::Vector2f viewSize;
	viewPos=mainGUI.view.getCenter();
	viewSize=mainGUI.view.getSize();
	if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left)){
		mainGUI.view.setCenter(sf::Vector2f(viewPos.x-2,viewPos.y));
		viewPos=mainGUI.view.getCenter();
	}
	if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right)){
		mainGUI.view.setCenter(sf::Vector2f(viewPos.x+2,viewPos.y));
		viewPos=mainGUI.view.getCenter();
	}
	if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up)){
		mainGUI.view.setCenter(sf::Vector2f(viewPos.x,viewPos.y-2));
		viewPos=mainGUI.view.getCenter();
	}
	if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down)){
		mainGUI.view.setCenter(sf::Vector2f(viewPos.x,viewPos.y+2));
		viewPos=mainGUI.view.getCenter();
	}
	/*sf::Event event;
	mainGUI.window.pollEvent(event);
	if(event.type==sf::Event::MouseWheelMoved){
		if(event.mouseWheel.delta>0)
			mainGUI.view.setSize(viewSize.x*+.11,viewSize.x);
	}*/

		return mainGUI;
}