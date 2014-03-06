#include "game.h"


int hell=0;
int main()
{
	//Structure held in game.h which holds the x and y dimensions of the field
	//and the sprite vector
	XY MainSprites;

	//sets initial number of squares in x an y dimensions
	MainSprites.xTotal=10;
	MainSprites.yTotal=20;

	//creates a font for debugging inside of the program
	sf::Font font;
	font.loadFromFile("arial.ttf");
	sf::Text text;
	text.setFont(font);
	text.setCharacterSize(24); 
	text.setColor(sf::Color::Red);
	text.setStyle(sf::Text::Bold | sf::Text::Underlined);

	//Vector of two points to hold the current mouse cursor position
	sf::Vector2f mousePos;
	
	//Texture used for the backround tile sprites
	sf::Texture backgroundTile;
	backgroundTile.loadFromFile("tile50x50.jpg");
	sf::RenderWindow window;
	std::vector<sf::VideoMode> modes = sf::VideoMode::getFullscreenModes();
	//Create Window with the first element of the modes vector, which holds optimal res, also set to fullscreen
	window.create(sf::VideoMode(modes[0]), "DNDGame",sf::Style::Fullscreen);
	MainSprites.view.setSize(sf::Vector2f(float(modes[0].width*.75),float(modes[0].height)));
	MainSprites.view.setCenter(sf::Vector2f(float(modes[0].width/2),float(modes[0].height/2)));

	int spriteSelected=0;
	sf::RectangleShape selectRect;

	//Create a sprite object and populate array with the Sprites while setting the position and texture of
	//each sprite
	sf::Sprite sprite;
	for (int i=0;i<MainSprites.xTotal*MainSprites.yTotal;i++){
		MainSprites.sprites.push_back(sprite);
		MainSprites.sprites[i].setTexture(backgroundTile);
		MainSprites.sprites[i].setPosition(sf::Vector2f(float(50*(i%MainSprites.xTotal)),(i%MainSprites.xTotal==0)?float(i/MainSprites.xTotal*50):float(std::floor(i/MainSprites.xTotal)*50)));
	}

	//Creates three gui objects, two inputs for the x and y dimensions of the playing field and a button object 
	//to tell when to lock in the entered values
	tgui::Gui gui(window);
	gui.setGlobalFont(font);
	tgui::EditBox::Ptr xBox(gui, "X Cells");
	tgui::EditBox::Ptr yBox(gui, "Y Cells");
	tgui::Button::Ptr  buttonBox(gui,"Return Box");
	xBox->load("TGUI/widgets/Babyblue.conf");
	yBox->load("TGUI/widgets/Babyblue.conf");
	buttonBox->load("TGUI/widgets/Babyblue.conf");
	xBox->setSize(400, 40);
	yBox->setSize(400, 40);
	xBox->setPosition(float(modes[0].width-400), 0.0);
	yBox->setPosition(float(modes[0].width-400), 50.0);
	buttonBox->setPosition(float(modes[0].width-400), 100.0);
	buttonBox->bindCallback(tgui::Button::LeftMouseClicked);
    buttonBox->setCallbackId(1);
	buttonBox->setText("Finish");

	//Set to true to exit main loop
	bool exit=false;

    while (window.isOpen() && exit==false){

		//Calls the drawGui function held in ViewGui.cpp, handles panning
		MainSprites=drawGui(MainSprites);

		sf::Event event;
        while (window.pollEvent(event)){

            if (event.type == sf::Event::Closed)
				window.close();
 
            // Pass the event to all gui widgets
            gui.handleEvent(event);
        }

		tgui::Callback callback;
        while (gui.pollCallback(callback)){

            // Make sure tha callback comes from the button
			if (callback.id == 1){
				tgui::EditBox::Ptr xCells = gui.get("X Cells");
				tgui::EditBox::Ptr yCells = gui.get("Y Cells");
               
				//store the input text and convert to ints to pass to x,y dimensions
				sf::String xNums = xCells->getText();
				sf::String yNums = yCells->getText();
				MainSprites.xTotal=std::stoi(xNums.toWideString());
				MainSprites.yTotal=std::stoi(yNums.toWideString());

				//clear the sprite array, then repopulate if new map boundries are set
				MainSprites.sprites.clear();
				for (int i=0;i<MainSprites.xTotal*MainSprites.yTotal;i++){
					MainSprites.sprites.push_back(sprite);
					MainSprites.sprites[i].setTexture(backgroundTile);
					MainSprites.sprites[i].setPosition(sf::Vector2f(float(50*(i%MainSprites.xTotal)),(i%MainSprites.xTotal==0)?float(i/MainSprites.xTotal*50):float(std::floor(i/MainSprites.xTotal)*50)));
				}  
			}
		}
        
		//if escape is pressed, exit the main loop
		if (sf::Keyboard::isKeyPressed(sf::Keyboard::Escape)){
			exit=true;
		}
		if(sf::Mouse::isButtonPressed(sf::Mouse::Button::Left)){
			//std::cout<<sf::Mouse::getPosition().y<<std::endl;
			mousePos=sf::Vector2f(sf::Mouse::getPosition());
			//std::cout<<mousePos.y<<std::endl;
			spriteSelected=selectSprite(MainSprites,window.mapPixelToCoords(sf::Mouse::getPosition(window)));
			text.setString(std::to_string(mousePos.x));
		}

		selectRect.setSize(sf::Vector2f(50.0,50.0));
		selectRect.setPosition(MainSprites.sprites[spriteSelected].getPosition());
		selectRect.setOutlineColor(sf::Color::Green);
		selectRect.setOutlineThickness(2.0);
		selectRect.setFillColor(sf::Color::Transparent);

		//Clear the window for drawing, draw the sprites, draw the gui on top of it, set the view, and then display
        window.clear();

		for(unsigned int i=0;i<MainSprites.sprites.size();i++){
			window.draw(MainSprites.sprites[i]);
		}
		window.draw(selectRect);
		gui.draw();

		window.setView(MainSprites.view);

		window.display();
    }

	    return 0;
}