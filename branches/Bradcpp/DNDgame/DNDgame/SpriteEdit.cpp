#include "game.h"

int selectSprite(XY mainSprites,sf::Vector2f mousePos){
	for(unsigned int i=0; i<mainSprites.sprites.size();i++){

		if(mainSprites.sprites[i].getGlobalBounds().contains(mousePos)){
			return i;
	}
}
	return 0;
}