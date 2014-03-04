#ifndef __game_H_INCLUDED__
#define __game_H_INCLUDED__
#include <SFML/Graphics.hpp>
#include <SFML/Window.hpp>
#include <iostream>
#include <TGUI/TGUI.hpp>
#include <vector>
struct XY{
		int xTotal;
		int yTotal;
		std::vector<sf::Sprite> sprites;
		sf::View view;
};
XY drawGui(XY mainGUI);
#endif