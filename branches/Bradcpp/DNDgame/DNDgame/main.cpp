#include "game.h"



int main()
{
	XY mainSprites;
	mainSprites.xTotal=10;
	mainSprites.yTotal=20;
	// Declare vector holding all the Fullscreen video modes
	std::vector<sf::VideoMode> modes = sf::VideoMode::getFullscreenModes();
	//Declare Window for drawing
	sf::RenderWindow window;
	sf::RenderWindow guiWindow;
	//Create Window with the first element of the modes vector, which holds optimal res, also set to fullscreen
	window.create(sf::VideoMode(modes[0]), "DNDGame",sf::Style::Fullscreen);
	mainSprites.view.setSize(sf::Vector2f(modes[0].width*.75,modes[0].height*.75));
	mainSprites.view.setCenter(sf::Vector2f(modes[0].width/2,modes[0].height/2));
	//guiWindow.create(sf::VideoMode(modes[0]), "Editor");
	bool exit=false;
	sf::Font font;
	font.loadFromFile("arial.ttf");
	sf::Text text;
	text.setFont(font);
	text.setCharacterSize(24); 
	text.setColor(sf::Color::Red);
	text.setStyle(sf::Text::Bold | sf::Text::Underlined);

	sf::Vector2i mousePos;
	
	sf::Texture backgroundTile;

	backgroundTile.loadFromFile("tile50x50.jpg");
	sf::Sprite sprite;

	for (int i=0;i<mainSprites.xTotal*mainSprites.yTotal;i++){
		mainSprites.sprites.push_back(sprite);
		mainSprites.sprites[i].setTexture(backgroundTile);
		mainSprites.sprites[i].setPosition(sf::Vector2f(50*(i%mainSprites.xTotal),(i%mainSprites.xTotal==0)?i/mainSprites.xTotal*50:std::floor(i/mainSprites.xTotal)*50));
	}

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
	buttonBox->setPosition(1500, 100);
	buttonBox->bindCallback(tgui::Button::LeftMouseClicked);
    buttonBox->setCallbackId(1);
	buttonBox->setText("Finish");
    while (window.isOpen() && exit==false)
    {
		mainSprites=drawGui(mainSprites);
		xBox->setPosition(modes[0].width-400, 0);
		yBox->setPosition(modes[0].width-400, 50);
		buttonBox->setPosition(modes[0].width-400, 100);
		mainSprites.sprites.clear();
		for (int i=0;i<mainSprites.xTotal*mainSprites.yTotal;i++){
		mainSprites.sprites.push_back(sprite);
		mainSprites.sprites[i].setTexture(backgroundTile);
		mainSprites.sprites[i].setPosition(sf::Vector2f(50*(i%mainSprites.xTotal),(i%mainSprites.xTotal==0)?i/mainSprites.xTotal*50:std::floor(i/mainSprites.xTotal)*50));
	}
		sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed)
                window.close();
 
            // Pass the event to all the widgets (if there would be widgets)
            gui.handleEvent(event);
        }
		tgui::Callback callback;
        while (gui.pollCallback(callback))
        {
            // Make sure tha callback comes from the button
            if (callback.id == 1)
            {
                // Get the username and password
                tgui::EditBox::Ptr xCells = gui.get("X Cells");
                tgui::EditBox::Ptr yCells = gui.get("Y Cells");
               
                sf::String xNums = xCells->getText();
                sf::String yNums = yCells->getText();
				if(!(mainSprites.xTotal=std::stoi(xNums.toWideString()))){
					mainSprites.xTotal=10;
				}
				mainSprites.yTotal=std::stoi(yNums.toWideString());

                    
            }
        }
		if (sf::Keyboard::isKeyPressed(sf::Keyboard::Escape))
			exit=true;
		if(sf::Mouse::isButtonPressed(sf::Mouse::Button::Left)){
			
			mousePos=sf::Mouse::getPosition(window);
			text.setString(std::to_string(mousePos.x));
		}
        window.clear();
		//window.setPosition(sf::Vector2i(1500,0));
		for(int i=0;i<mainSprites.sprites.size();i++)
			window.draw(mainSprites.sprites[i]);
		gui.draw();
		window.setView(mainSprites.view);
		window.display();
		//guiWindow.display();
    }

	    return 0;
}