// Yu Chiu
// Program#3

#include <gl/glut.h> 
#include <math.h>
void drawtrianglefan()
{
	glShadeModel(GL_FLAT);
	glBegin(GL_TRIANGLE_FAN);
	glVertex2f(2, 2);
	glVertex2f(5, 5);
	glColor3f(1.0, 0.0, 0.0);
	glVertex2f(6, 2.5);
	glColor3f(0.0, 0.0, 1.0);
	glVertex2f(4.5, 0);
	glColor3f(0.0, 1.0, 0.0);
	glVertex2f(1.5, -1.0);
	glEnd();
}
void drawtrianglestrip() 
{
	glShadeModel(GL_FLAT);
	glBegin(GL_TRIANGLE_STRIP);
	glVertex2f(-8.0, 5.0);
	glVertex2f(-6, 2.0);
	glColor3f(1, 0.0, 0.0);
	glVertex2f(-3, 3);
	glColor3f(0.0, 0.0, 1);
	glVertex2f(0.0, -1.5);
	glColor3f(0.0, 1.0, 0.0);
	glVertex2f(2, 2);
	glEnd();
}
void drawtriangle(){
	glShadeModel(GL_FLAT);
	glBegin(GL_TRIANGLES);
	glColor3f(0.0, 1.0, 0.0);
	glVertex2f(-6.0, 6.0);
	glVertex2f(-7.5, 8.5);
	glVertex2f(-8.0, 5.0);
	glEnd();
}
void animation(float x, float y, float z)
{
	static float i = 0, f = 0,j=0;
	i += 0.1;
	f += 0.03;
	j += 0.01;
	if (i > 360)
		i = 0;
	if (f > 360)
		f = 0;
	if (j > 360)
		j = 0;

	glPushMatrix();
	glTranslatef(x, y, z);
	glRotatef(j, 0, 1, 0);


	glPushMatrix();
	glTranslatef(0, 0, 0.5);
	glRotatef(f, 0, 0, 1);

	glPushMatrix();
	glRotatef(i, 1,0, 0);
	glTranslatef(0, 0, 0.5);
	glScalef(0.1, 0.05, 1);
	drawtrianglestrip();//level3 rotates round x
	glPopMatrix();
	
	glScalef(0.1, 0.1, 0.1);
	drawtrianglefan();//level 2 rotates round z
	glPopMatrix();

	glScalef(0.1, 0.1, 0.1);
	drawtriangle();//level1 rotate round y
	glPopMatrix();
}
void renderScene(void)
{
	glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
	glLoadIdentity();

	animation(0, 0, -5);

	glutSwapBuffers();
}
void changeSize(int w, int h) {

	// prevent divisor to be 0
	if (h == 0)
		h = 1;
	float ratio = 1.0* w / h;

	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();

	// setting the size of viewport
	glViewport(0, 0, w, h);

	//setting up the correct projection matrix
	gluPerspective(45, ratio, 1, 1000);

	//setting up modelview matrix below
	glMatrixMode(GL_MODELVIEW);
	glLoadIdentity();
	gluLookAt(0.0, 0.0, 5.0, 0.0, 0.0, -1.0, 0.0f, 1.0f, 0.0f);//setting the view
}
int main(int argc, char * argv[])
{
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DEPTH | GLUT_DOUBLE | GLUT_RGBA);
	glutInitWindowPosition(100, 100);
	glutInitWindowSize(300, 300);
	glutCreateWindow("Animation");
	glutDisplayFunc(renderScene);
	glutIdleFunc(renderScene);
	glutReshapeFunc(changeSize);
	glEnable(GL_DEPTH_TEST);
	glutMainLoop();
	return 0;
}
