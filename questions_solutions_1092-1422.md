# Questions and solutions: IDs 1092–1422

## ID 1092

**Question:** $12\cdot\ \lim_{x\to2}\left[\frac{1}{x-2}-\frac{1}{\ln(x-1)}\right]$

**Solution:** $12\cdot\ \lim_{x\to2}\left[\frac{1}{x-2}-\frac{1}{\ln(x-1)}\right]=\lim_{x\to2}\frac{\ln(x-1)-(x-2)}{(x-2)\ln(x-1)}$\\$=\lim_{x\to2}\frac{\frac{1}{x-1}-1}{1\cdot\ln(x-1)+(x-2)\frac{1}{x-1}}$\\$=\lim_{x\to2}\frac{x-1}{x-1}\cdot\frac{2-x}{(x-2)+(x-1)\ln(x-1)}$\\$=\lim_{x\to2}\frac{2-x}{x-2+(x-1)\ln(x-1)}$\\$=\lim_{x\to2}\frac{-1}{1+1+\ln(x-1)};\ [L'Hospital]$\\$=-\frac{1}{2}\ (Ans.)$

**Final answer:** $-\frac{1}{2}$

## ID 1093

**Question:** $13\cdot\ \lim_{x\to\infty}\frac{3x^2-\sin2x}{x^2+5}$

**Solution:** $13\cdot\ \lim_{x\to\infty}\frac{3x^2-\sin2x}{x^2+5}$\\আমরা জানি, $-1\le -\sin2x\le1;\ (\text{যেহেতু} x>0)$\\$3x^2-1\le3x^2-\sin2x\le3x^2+1$\\$\frac{3x^2-1}{x^2+5}\le\frac{3x^2-\sin2x}{x^2+5}\le\frac{3x^2+1}{x^2+5}$\\এখন, $\lim_{x\to\infty}\frac{3x^2-1}{x^2+5}=\lim_{x\to\infty}\frac{3-\frac{1}{x^2}}{1+\frac{5}{x^2}}=3$\\$\text{এবং} \lim_{x\to\infty}\frac{3x^2+1}{x^2+5}=\lim_{x\to\infty}\frac{3+\frac{1}{x^2}}{1+\frac{5}{x^2}}=3$\\$\therefore$ স্যান্ডউইচ উপপাদ্য অনুসারে পাই,\\$\lim_{x\to\infty}\frac{3x^2-\sin2x}{x^2+5}=3\cdot\ (\text{প্রমাণিত})$

**Final answer:** $3$

## ID 1094

**Question:** $14\cdot\ \lim_{x\to\infty}\frac{\sqrt{x^2+2}}{3x-6}$

**Solution:** $14\cdot\ \lim_{x\to\infty}\frac{\sqrt{x^2+2}}{3x-6}=\lim_{x\to\infty}\frac{x\sqrt{1+\frac{2}{x^2}}}{x\left(3-\frac{6}{x}\right)}$\\$=\frac{\lim_{x\to\infty}\sqrt{1+\frac{2}{x^2}}}{\lim_{x\to\infty}\left(3-\frac{6}{x}\right)}=\frac{\sqrt{1+0}}{3-0}=\frac{1}{3}\ (Ans.)$

**Final answer:** $\frac{1}{3}$

## ID 1095

**Question:** $15\cdot\ \lim_{x\to0}\frac{2(b-\sqrt{b^2+x^2})}{x^2}$

**Solution:** $15\cdot\ \lim_{x\to0}\frac{2(b-\sqrt{b^2+x^2})}{x^2}$\\$=\lim_{x\to0}\frac{2(b-\sqrt{b^2+x^2})(b+\sqrt{b^2+x^2})}{x^2(b+\sqrt{b^2+x^2})}$\\$=\lim_{x\to0}\frac{2(b^2-b^2-x^2)}{x^2(b+\sqrt{b^2+x^2})}$\\$=\frac{-2}{(b+\sqrt{b^2+0})}=-\frac{1}{b}\ (Ans.)$

**Final answer:** $-\frac{1}{b}$

## ID 1096

**Question:** $16\cdot\ \lim_{x\to\infty}\frac{e^{\frac{1}{x^2}}-1}{2\tan^{-1}(x^2)-\pi}$

**Solution:** $16\cdot\ \lim_{x\to\infty}\frac{e^{\frac{1}{x^2}}-1}{2\tan^{-1}(x^2)-\pi}$\\$=\lim_{x\to\infty}\frac{e^{\frac{1}{x^2}}\left(-\frac{2}{x^3}\right)}{\frac{4x}{1+x^4}}$\\$[L'Hospital's Rule]$\\$=\lim_{x\to\infty}\frac{-e^{\frac{1}{x^2}}(1+x^4)}{2x^4}=\lim_{x\to\infty}-\frac{e^{\frac{1}{x^2}}}{2}\left(1+\frac{1}{x^4}\right)$\\$=-\frac{e^0}{2}(1+0)=-\frac{1}{2}\ (Ans.)$

**Final answer:** $-\frac{1}{2}$

## ID 1097

**Question:** $17\cdot\ \lim_{x\to0}\frac{2e^x-2e^{-5x}+ax}{x^2}$ সীমাটি বিদ্যমান থাকার জন্য $a$ এর মান নির্ণয় কর এবং সীমার মান নির্ণয় কর।

**Solution:** $17\cdot\ \lim_{x\to0}\frac{2e^x-2e^{-5x}+ax}{x^2}$\\$=\lim_{x\to0}\frac{1}{x^2}\left\{2\left(1+\frac{x}{1!}+\frac{x^2}{2!}+\frac{x^3}{3!}+\cdots\right)-2\left(1-\frac{5x}{1!}+\frac{(5x)^2}{2!}-\frac{(5x)^3}{3!}+\cdots\right)+ax\right\}$\\$=\lim_{x\to0}\left\{\frac{(2+10+a)x}{x^2}+\frac{(2-50)x^2}{2!x^2}+x \text{ এর উচ্চতর ঘাতের সমষ্টি পদ}\right\}$\\$=\lim_{x\to0}\left\{\frac{12+a}{x}-24+x \text{ এর উচ্চতর ঘাতের সমষ্টি পদ}\right\}$\\প্রদত্ত সীমা বিদ্যমান থাকবে যদি $12+a=0$ হয়,\\$\text{বা,} a=-12$ হয়।\\অতএব, সীমার মান $=-24$। (Ans.)

**Final answer:** $a=-12$; সীমার মান $=-24$

## ID 1098

**Question:** $\frac{d}{dx}(\sqrt{x})$

**Solution:** $1.(i)$ মনে করি, $f(x)=\sqrt{x}$\\$\therefore f(x+h)=\sqrt{x+h}$\\সংজ্ঞানুসারে আমরা পাই,\\$\frac{d}{dx}\{f(x)\}=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$\\$\therefore \frac{d}{dx}(\sqrt{x})=\lim_{h\to0}\frac{\sqrt{x+h}-\sqrt{x}}{h}$\\$=\lim_{h\to0}\frac{(x+h)^{\frac{1}{2}}-x^{\frac{1}{2}}}{h}$\\$=\lim_{h\to0}\frac{x^{\frac{1}{2}}\left(1+\frac{h}{x}\right)^{\frac{1}{2}}-x^{\frac{1}{2}}}{h}$\\$=\lim_{h\to0}\frac{x^{\frac{1}{2}}\left\{1+\frac{h}{2x}+\frac{h^2}{x^2}\cdot\frac{\frac{1}{2}\left(\frac{1}{2}-1\right)}{2!}+\cdots-1\right\}}{h}$\\$=\lim_{h\to0}\frac{x^{\frac{1}{2}}\left(\frac{h}{2x}-\frac{h^2}{8x^2}+\cdots\right)}{h}$\\$=\lim_{h\to0}\left(\frac{1}{2x^{\frac{1}{2}}}-\frac{h}{8x^{\frac{3}{2}}}+\cdots\right)=\frac{1}{2x^{\frac{1}{2}}}$\\$\therefore \frac{d}{dx}(\sqrt{x})=\frac{1}{2x^{\frac{1}{2}}}=\frac{1}{2\sqrt{x}}\ (Ans.)$\\বিকল্প সমাধান:\\$\frac{d}{dx}(\sqrt{x})=\lim_{h\to0}\frac{\sqrt{x+h}-\sqrt{x}}{h}$\\$=\lim_{h\to0}\frac{(\sqrt{x+h}+\sqrt{x})(\sqrt{x+h}-\sqrt{x})}{h(\sqrt{x+h}+\sqrt{x})}$\\$=\lim_{h\to0}\frac{x+h-x}{h(\sqrt{x+h}+\sqrt{x})}=\lim_{h\to0}\frac{h}{h(\sqrt{x+h}+\sqrt{x})}$\\$=\lim_{h\to0}\frac{1}{\sqrt{x+h}+\sqrt{x}}=\frac{1}{\sqrt{x}+\sqrt{x}}=\frac{1}{2\sqrt{x}}\ (Ans.)$

**Final answer:** $\frac{1}{2\sqrt{x}}$

## ID 1099

**Question:** $\frac{d}{dx}(e^{mx})$

**Solution:** $(iii)$ মনে করি, $f(x)=e^{mx}$\\$\therefore f(x+h)=e^{m(x+h)}$\\$\frac{d}{dx}\{f(x)\}=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$\\$\therefore \frac{d}{dx}(e^{mx})=\lim_{h\to0}\frac{e^{m(x+h)}-e^{mx}}{h}$\\$=\lim_{h\to0}\frac{e^{mx}e^{mh}-e^{mx}}{h}=\lim_{h\to0}e^{mx}\left(\frac{e^{mh}-1}{h}\right)$\\$=\lim_{h\to0}e^{mx}\cdot\frac{1}{h}\left\{\left(1+\frac{mh}{1!}+\frac{m^2h^2}{2!}+\frac{m^3h^3}{3!}+\cdots\right)-1\right\}$\\$=\lim_{h\to0}e^{mx}\cdot\frac{1}{h}\left(mh+\frac{m^2h^2}{2!}+\frac{m^3h^3}{3!}+\cdots\right)$\\$=\lim_{h\to0}e^{mx}\left(m+\frac{m^2h}{2!}+\frac{m^3h^2}{3!}+\cdots\right)=me^{mx}$\\$\therefore \frac{d}{dx}(e^{mx})=me^{mx}\ (Ans.)$

**Final answer:** $me^{mx}$

## ID 1100

**Question:** $\frac{d}{dx}(\ln x)$

**Solution:** $(iv)$ মনে করি, $f(x)=\ln x$\\$\therefore f(x+h)=\ln(x+h)$\\সংজ্ঞানুসারে আমরা পাই পাই,\\$\frac{d}{dx}\{f(x)\}=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$\\$\therefore \frac{d}{dx}(\ln x)=\lim_{h\to0}\frac{\ln(x+h)-\ln x}{h}$\\$=\lim_{h\to0}\frac{1}{h}\ln\left(\frac{x+h}{x}\right)\quad [\text{কারণ} \ln\left(\frac{a}{b}\right)=\ln a-\ln b]$\\$=\lim_{h\to0}\frac{1}{h}\ln\left(1+\frac{h}{x}\right)$\\$=\lim_{h\to0}\frac{1}{h}\left\{\frac{h}{x}-\frac{(\frac{h}{x})^2}{2}+\frac{(\frac{h}{x})^3}{3}-\cdots\right\}$\\$=\lim_{h\to0}\frac{1}{h}\left(\frac{h}{x}-\frac{1}{2}\frac{h^2}{x^2}+\frac{1}{3}\frac{h^3}{x^3}-\cdots\right)$\\$=\lim_{h\to0}\frac{h}{h}\left(\frac{1}{x}-\frac{1}{2}\frac{h}{x^2}+\frac{1}{3}\frac{h^2}{x^3}-\cdots\right)$\\$=\lim_{h\to0}\left(\frac{1}{x}-\frac{1}{2}\frac{h}{x^2}+\frac{1}{3}\frac{h^2}{x^3}-\cdots\right)$\\$=\frac{1}{x},\ (x>0)$    $\therefore \frac{d}{dx}(\ln x)=\frac{1}{x}\ (Ans.)$

**Final answer:** $\frac{1}{x}$

## ID 1101

**Question:** $\frac{d}{dx}(\cos2x)$

**Solution:** $(v)$ মনে করি, $f(x)=\cos2x$\\$\therefore f(x+h)=\cos2(x+h)$\\সংজ্ঞানুসারে আমরা পাই পাই,\\$\frac{d}{dx}\{f(x)\}=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$\\$\therefore \frac{d}{dx}(\cos2x)=\lim_{h\to0}\frac{\cos2(x+h)-\cos2x}{h}$\\$=\lim_{h\to0}\frac{2\sin\left(\frac{2x+2h+2x}{2}\right)\sin\left(\frac{2x-2x-2h}{2}\right)}{h}$\\$=\lim_{h\to0}\frac{2\sin(2x+h)\sin(-h)}{h}$\\$=-\lim_{h\to0}2\sin(2x+h)\times\lim_{h\to0}\frac{\sin h}{h}$\\$=-2\sin(2x+0)\times1=-2\sin2x\ (Ans.)$

**Final answer:** $-2\sin2x$

## ID 1102

**Question:** $\frac{d}{dx}(\sin2x)$

**Solution:** $(vi)$ মনে করি, $f(x)=\sin2x$\\$\therefore f(x+h)=\sin2(x+h)$\\সংজ্ঞানুসারে আমরা পাই পাই,\\$\frac{d}{dx}\{f(x)\}=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$\\$\therefore \frac{d}{dx}(\sin2x)=\lim_{h\to0}\frac{\sin2(x+h)-\sin2x}{h}$\\$=\lim_{h\to0}\frac{\sin(2x+2h)-\sin2x}{h}$\\$=\lim_{h\to0}\frac{1}{h}\left[2\cos\left(\frac{2x+2h+2x}{2}\right)\sin\left(\frac{2x+2h-2x}{2}\right)\right]$\\$=\lim_{h\to0}\left[\frac{1}{h}2\cos(2x+h)\sin h\right]$\\$=2\left[\lim_{h\to0}\cos(2x+h)\lim_{h\to0}\left(\frac{\sin h}{h}\right)\right]$\\$=2\cos2x\cdot1\quad [\therefore \lim_{\theta\to0}\frac{\sin\theta}{\theta}=1]=2\cos2x$\\$\therefore \frac{d}{dx}(\sin2x)=2\cos2x\ (Ans.)$

**Final answer:** $2\cos2x$

## ID 1103

**Question:** $\frac{d}{dx}(\tan2x)$

**Solution:** $(vii)$ মনে করি, $f(x)=\tan2x$\\$\therefore f(x+h)=\tan2(x+h)=\tan(2x+2h)$\\সংজ্ঞানুসারে আমরা পাই পাই,\\$\frac{d}{dx}\{f(x)\}=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$\\$\therefore \frac{d}{dx}(\tan2x)=\lim_{h\to0}\frac{\tan(2x+2h)-\tan2x}{h}$\\$=\lim_{h\to0}\frac{1}{h}\left[\frac{\sin(2x+2h)}{\cos(2x+2h)}-\frac{\sin2x}{\cos2x}\right]$\\$=\lim_{h\to0}\frac{1}{h}\left[\frac{\sin(2x+2h)\cos2x-\sin2x\cos(2x+2h)}{\cos(2x+2h)\cos2x}\right]$\\$=\lim_{h\to0}\frac{1}{h}\frac{\sin(2x+2h-2x)}{\cos(2x+2h)\cos2x}$\\$=\lim_{h\to0}\frac{\sin2h}{h}\times\lim_{h\to0}\frac{1}{\cos(2x+2h)\cos2x}$\\$=\lim_{2h\to0}\frac{\sin2h}{2h}\times2\times\lim_{h\to0}\frac{1}{\cos(2x+2h)\cos2x}$\\$=1\times2\times\frac{1}{\cos(2x+0)\cos2x}=\frac{2}{\cos^2 2x}$\\$=2\sec^2 2x\ (Ans.)$

**Final answer:** $2\sec^2 2x$

## ID 1104

**Question:** $\frac{d}{dx}(\cos3x)$

**Solution:** $(viii)$ মনে করি, $f(x)=\cos3x$\\$\therefore f(x+h)=\cos3(x+h)$\\সংজ্ঞানুসারে আমরা পাই পাই,\\$\frac{d}{dx}\{f(x)\}=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$\\$=\lim_{h\to0}\frac{\cos3(x+h)-\cos3x}{h}$\\$=\lim_{h\to0}\frac{1}{h}\left[2\sin\left(\frac{3x+3h+3x}{2}\right)\sin\left(\frac{3x-3x-3h}{2}\right)\right]$\\$=\lim_{h\to0}\frac{1}{h}\left[2\sin\left(3x+\frac{3h}{2}\right)\sin\left(-\frac{3h}{2}\right)\right]$\\$=\lim_{h\to0}\frac{-\sin\frac{3h}{2}}{\frac{3h}{2}}\cdot3\lim_{h\to0}\sin\left(3x+\frac{3h}{2}\right)$\\$=-3\lim_{\frac{3h}{2}\to0}\left(\frac{\sin\frac{3h}{2}}{\frac{3h}{2}}\right)\times\lim_{h\to0}\sin\left(3x+\frac{3h}{2}\right)$\\$=-3\cdot1\cdot\sin3x=-3\sin3x$\\$\therefore \frac{d}{dx}(\cos3x)=-3\sin3x\ (Ans.)$

**Final answer:** $-3\sin3x$

## ID 1105

**Question:** $\frac{d}{dx}(\tan3x)$

**Solution:** $(ix)$ মনে করি, $f(x)=\tan3x$\\$\therefore f(x+h)=\tan3(x+h)$\\সংজ্ঞানুসারে আমরা পাই পাই,\\$\frac{d}{dx}\{f(x)\}=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$\\$\therefore \frac{d}{dx}(\tan3x)=\lim_{h\to0}\frac{\tan\{3(x+h)\}-\tan3x}{h}$\\$=\lim_{h\to0}\frac{1}{h}\left[\frac{\sin3(x+h)}{\cos3(x+h)}-\frac{\sin3x}{\cos3x}\right]$\\$=\lim_{h\to0}\frac{1}{h}\left[\frac{\sin3(x+h)\cos3x-\cos3(x+h)\sin3x}{\cos3(x+h)\cos3x}\right]$\\$=\lim_{h\to0}\frac{1}{h}\left[\frac{\sin\{3(x+h-x)\}}{\cos3x\cos3(x+h)}\right]$\\$=\lim_{h\to0}\frac{1}{h}\frac{\sin3h}{\cos3x\cos3(x+h)}$\\$=3\lim_{h\to0}\frac{\sin3h}{3h}\frac{1}{\cos3x\cos3(x+h)}$\\$=3\frac{\lim_{h\to0}\left(\frac{\sin3h}{3h}\right)}{\lim_{h\to0}\cos3x\cos3(x+h)}$\\$=\frac{3}{\cos3x\cos3x}\quad [\therefore \lim_{\theta\to0}\frac{\sin\theta}{\theta}=1]$\\$=\frac{3}{\cos^2 3x}=3\sec^2 3x\ (Ans.)$

**Final answer:** $3\sec^2 3x$

## ID 1106

**Question:** $\frac{d}{dx}(\tan4x)$

**Solution:** $(x)$ মনে করি, $f(x)=\tan4x$\\$\therefore f(x+h)=\tan(4x+4h)$\\সংজ্ঞানুসারে আমরা পাই পাই,\\$\frac{d}{dx}f(x)=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$\\$\therefore \frac{d}{dx}(\tan4x)=\lim_{h\to0}\frac{\tan(4x+4h)-\tan4x}{h}$\\$=\lim_{h\to0}\frac{\frac{\sin(4x+4h)}{\cos(4x+4h)}-\frac{\sin4x}{\cos4x}}{h}$\\$=\lim_{h\to0}\frac{\sin(4x+4h)\cos4x-\cos(4x+4h)\sin4x}{h\cos(4x+4h)\cos4x}$\\$=\lim_{h\to0}\frac{\sin(4x+4h-4x)}{h\cos(4x+4h)\cos4x}$\\$=4\lim_{4h\to0}\frac{\sin4h}{4h}\lim_{h\to0}\frac{1}{\cos(4x+4h)\cos4x}$\\$=4\cdot1\cdot\frac{1}{\cos4x\cos4x}=\frac{4}{\cos^2 4x}$\\$\therefore \frac{d}{dx}(\tan4x)=4\sec^2 4x\ (Ans.)$

**Final answer:** $4\sec^2 4x$

## ID 1107

**Question:** $\frac{d}{dx}(\sec2x)$

**Solution:** $(xi)$ মনে করি, $f(x)=\sec2x$\\$\therefore f(x+h)=\sec(2x+2h)$\\সংজ্ঞানুসারে আমরা পাই পাই,\\$\frac{d}{dx}\{f(x)\}=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$\\$\therefore \frac{d}{dx}(\sec2x)=\lim_{h\to0}\frac{\sec(2x+2h)-\sec2x}{h}$\\$=\lim_{h\to0}\frac{1}{h}\left[\frac{1}{\cos(2x+2h)}-\frac{1}{\cos2x}\right]$\\$=\lim_{h\to0}\frac{1}{h}\left[\frac{\cos2x-\cos(2x+2h)}{\cos2x\cdot\cos(2x+2h)}\right]$\\$=\lim_{h\to0}\frac{1}{h}\left[\frac{2\sin\left(\frac{2x+2x+2h}{2}\right)\cdot\sin\left(\frac{2x+2h-2x}{2}\right)}{\cos2x\cdot\cos(2x+2h)}\right]$\\$=\lim_{h\to0}\frac{1}{h}\left[\frac{2\sin(2x+h)\cdot\sin h}{\cos2x\cdot\cos(2x+2h)}\right]$\\$=\lim_{h\to0}\frac{2}{\cos2x\cdot\cos(2x+2h)}\frac{\sin(2x+h)\cdot\sin h}{h}$\\$=2\cdot\frac{\lim_{h\to0}\sin(2x+h)\cdot\lim_{h\to0}\left(\frac{\sin h}{h}\right)}{\lim_{h\to0}\cos2x\cdot\cos(2x+2h)}$\\$=2\cdot\frac{\sin2x\cdot1}{\cos2x\cdot\cos2x}$\\$\therefore \frac{d}{dx}(\sec2x)=2\tan2x\cdot\sec2x\ (Ans.)$

**Final answer:** $2\tan2x\cdot\sec2x$

## ID 1108

**Question:** $\frac{d}{dx}(\sec ax)$

**Solution:** $(xii)$ মনে করি, $f(x)=\sec ax$\\$\therefore f(x+h)=\sec(ax+ah)$\\সংজ্ঞানুসারে আমরা পাই পাই,\\$\frac{d}{dx}\{f(x)\}=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$\\$\therefore \frac{d}{dx}(\sec ax)=\lim_{h\to0}\frac{\sec(ax+ah)-\sec ax}{h}$\\$=\lim_{h\to0}\frac{1}{h}\left[\frac{1}{\cos(ax+ah)}-\frac{1}{\cos ax}\right]$\\$=\lim_{h\to0}\frac{1}{h}\left[\frac{\cos ax-\cos(ax+ah)}{\cos ax\cdot\cos(ax+ah)}\right]$\\$=\lim_{h\to0}\frac{1}{h}\left[\frac{2\sin\left(\frac{ax+ax+ah}{2}\right)\cdot\sin\left(\frac{ax+ah-ax}{2}\right)}{\cos ax\cdot\cos(ax+ah)}\right]$\\$=\lim_{h\to0}\frac{2}{h}\left[\frac{\sin\left(ax+\frac{ah}{2}\right)\cdot\sin\left(\frac{ah}{2}\right)}{\cos ax\cdot\cos(ax+ah)}\right]$\\$=a\lim_{h\to0}\frac{2}{ah}\left[\frac{\sin\left(ax+\frac{ah}{2}\right)\cdot\sin\left(\frac{ah}{2}\right)}{\cos ax\cdot\cos(ax+ah)}\right]$\\$=a\frac{\lim_{h\to0}\sin\left(ax+\frac{ah}{2}\right)\cdot\lim_{h\to0}\frac{\sin\frac{ah}{2}}{\frac{ah}{2}}}{\lim_{h\to0}\cos ax\cdot\lim_{h\to0}\cos(ax+ah)}$\\$=a\cdot\frac{\sin ax\cdot1}{\cos ax\cdot\cos ax}$\\$\therefore \frac{d}{dx}(\sec ax)=a\tan ax\cdot\sec ax\ (Ans.)$

**Final answer:** $a\tan ax\cdot\sec ax$

## ID 1109

**Question:** $\frac{d}{dx}(\cos ax)$

**Solution:** $(xiii)$ মনে করি, $f(x)=\cos ax$\\$\therefore f(x+h)=\cos a(x+h)=\cos(ax+ah)$\\সংজ্ঞানুসারে আমরা পাই পাই,\\$\frac{d}{dx}\{f(x)\}=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$\\$\therefore \frac{d}{dx}(\cos ax)=\lim_{h\to0}\frac{\cos(ax+ah)-\cos ax}{h}$\\$=\lim_{h\to0}\frac{1}{h}\left[2\sin\frac{ax+ah+ax}{2}\sin\frac{ax-ax-ah}{2}\right]$\\$=2\lim_{h\to0}\sin\left(ax+\frac{ah}{2}\right)\times\left\{-\lim_{h\to0}\frac{\sin(ah/2)}{ah/2}\frac{a}{2}\right\}$\\$=2\sin(ax+0)\cdot\left(-1\cdot\frac{a}{2}\right)=-a\sin ax\ (Ans.)$

**Final answer:** $-a\sin ax$

## ID 1110

**Question:** $\frac{d}{dx}(\cosec ax)$

**Solution:** $(xiv)$ মনে করি, $f(x)=\cosec ax$\\$\therefore f(x+h)=\cosec(ax+ah)$\\অন্তরক সহগের সংজ্ঞা হতে পাই,\\$\frac{d}{dx}\{f(x)\}=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$\\$\therefore \frac{d}{dx}(\cosec ax)=\lim_{h\to0}\frac{\cosec(ax+ah)-\cosec ax}{h}$\\$=\lim_{h\to0}\frac{1}{h}\left[\frac{1}{\sin(ax+ah)}-\frac{1}{\sin ax}\right]$\\$=\lim_{h\to0}\frac{\sin ax-\sin(ax+ah)}{h\sin(ax+ah)\sin ax}$\\$=\lim_{h\to0}\frac{2\sin\frac{ax-ax-ah}{2}\cos\frac{ax+ax+ah}{2}}{h\sin(ax+ah)\sin ax}$\\$=\lim_{h\to0}\frac{2\sin\left(-\frac{ah}{2}\right)\cos\left(ax+\frac{ah}{2}\right)}{h\sin(ax+ah)\sin ax}$\\$=-2\lim_{h\to0}\frac{\sin ah/2}{ah/2}\times\frac{a}{2}\times\lim_{h\to0}\frac{\cos\left(ax+\frac{ah}{2}\right)}{\sin(ax+ah)\sin ax}$\\$=-2\times\frac{a}{2}\times\frac{\cos(ax+0)}{\sin(ax+0)\sin ax}$\\$=-a\frac{\cos ax}{\sin ax\sin ax}$\\$=-a\cot ax\cosec ax\ (Ans.)$

**Final answer:** $-a\cot ax\cosec ax$

## ID 1111

**Question:** $\frac{d}{dx}(2x^2+3x+1)$

**Solution:** $(xvi)$ ধরি, $f(x)=2x^2+3x+1$\\$f(x+h)=2(x+h)^2+3(x+h)+1$\\মূল নিয়মের সাহায্যে অন্তরক সহগ হতে পাই,\\$\frac{d}{dx}[f(x)]=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$\\$\therefore \frac{d}{dx}(2x^2+3x+1)=\lim_{h\to0}\frac{2(x+h)^2+3(x+h)+1-(2x^2+3x+1)}{h}$\\$=\lim_{h\to0}\frac{2x^2+4xh+2h^2+3x+3h+1-2x^2-3x-1}{h}$\\$=\lim_{h\to0}\frac{4xh+2h^2+3h}{h}=\lim_{h\to0}\frac{h(4x+2h+3)}{h}$\\$=\lim_{h\to0}(4x+2h+3)=4x+0+3=4x+3\ (Ans.)$

**Final answer:** $4x+3$

## ID 1112

**Question:** $\frac{d}{dx}(x^3+2x)$

**Solution:** $(xvii)$ মনে করি, $f(x)=x^3+2x$\\$\therefore f(x+h)=(x+h)^3+2(x+h)$\\সংজ্ঞানুসারে আমরা পাই,\\$\frac{d}{dx}\{f(x)\}=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$\\$\therefore \frac{d}{dx}(x^3+2x)=\lim_{h\to0}\frac{(x+h)^3+2(x+h)-x^3-2x}{h}$\\$=\lim_{h\to0}\frac{x^3+3x^2h+3xh^2+h^3+2x+2h-x^3-2x}{h}$\\$=\lim_{h\to0}\frac{(3x^2h+3xh^2+h^3+2h)}{h}$\\$=\lim_{h\to0}(3x^2+3xh+h^2+2)$\\$=3x^2+2\ (Ans.)$

**Final answer:** $3x^2+2$

## ID 1113

**Question:** $\frac{d}{dx}(\cos7x)$

**Solution:** $(xviii)$ প্রদত্ত ফাংশন $=\sin\left(\frac{\pi}{2}-7x\right)=\cos7x$\\$\text{ধরি,} g(x)=\cos7x$\\$\therefore g(x+h)=\cos7(x+h)=\cos(7x+7h)$\\সংজ্ঞানুসারে আমরা পাই,\\$\frac{d}{dx}\{g(x)\}=\lim_{h\to0}\frac{g(x+h)-g(x)}{h}$\\$\therefore \frac{d}{dx}(\cos7x)=\lim_{h\to0}\frac{\cos(7x+7h)-\cos7x}{h}$\\$=\lim_{h\to0}\frac{1}{h}\left[2\sin\left(\frac{7x+7h+7x}{2}\right)\sin\left(\frac{7x-7x-7h}{2}\right)\right]$\\$=\lim_{h\to0}\frac{1}{h}\left[2\sin\left(7x+\frac{7h}{2}\right)\sin\left(-\frac{7h}{2}\right)\right]$\\$=\lim_{h\to0}\frac{-\sin\frac{7h}{2}}{\frac{7h}{2}}\cdot7\lim_{h\to0}\sin\left(7x+\frac{7h}{2}\right)$\\$=-7\lim_{\frac{7h}{2}\to0}\left(\frac{\sin\frac{7h}{2}}{\frac{7h}{2}}\right)\cdot\lim_{h\to0}\sin\left(7x+\frac{7h}{2}\right)$\\$=-7\cdot1\cdot\sin7x=-7\sin7x$\\$\therefore \frac{d}{dx}(\cos7x)=-7\sin7x\ (Ans.)$

**Final answer:** $-7\sin7x$

## ID 1114

**Question:** $\frac{d}{dx}(\ln px),\ p=3$

**Solution:** $(xix)$ দেওয়া আছে, $f(x)=\ln px$\\$p=3$ হলে, $f(x)=\ln3x$. $\therefore f(x+h)=\ln3(x+h)$\\মূল নিয়মের সাহায্যে অন্তরক সহগ হতে পাই,\\$\frac{d}{dx}\{f(x)\}=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$\\$\therefore \frac{d}{dx}\{\ln(3x)\}=\lim_{h\to0}\frac{\ln3(x+h)-\ln3x}{h}$\\$=\lim_{h\to0}\frac{\ln(3x+3h)-\ln(3x)}{h}$\\$=\lim_{h\to0}\frac{\ln\left(\frac{3x+3h}{3x}\right)}{h}=\lim_{h\to0}\frac{\ln\left(1+\frac{h}{x}\right)}{h}$\\$=\lim_{h\to0}\frac{\left(\frac{h}{x}-\frac{h^2}{2x^2}+\frac{h^3}{3x^3}\cdots\right)}{h}$\\$=\lim_{h\to0}\left(\frac{1}{x}-\frac{h}{2x^2}+\frac{h^2}{3x^3}\cdots\right)=\frac{1}{x}\ (Ans.)$

**Final answer:** $\frac{1}{x}$

## ID 1115

**Question:** $\frac{d}{dx}(\log_5x)$

**Solution:** $(xx)$ দেওয়া আছে,\\$f(x)=\log_5x=\log_5e\times\log_ex=\log_5e\times\ln x$\\$\therefore f(x+h)=\log_5e\times\ln(x+h)$\\সংজ্ঞানুসারে আমরা পাই,\\$\frac{dy}{dx}\{f(x)\}=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$\\$\therefore \frac{d}{dx}(\log_5x)$\\$=\lim_{h\to0}\frac{\log_5e\times\ln(x+h)-\log_5e\times\ln x}{h}$\\$=\lim_{h\to0}\log_5e\frac{\ln(x+h)-\ln x}{h}$\\$=\log_5e\lim_{h\to0}\frac{\ln\left(\frac{x+h}{x}\right)}{h}\quad [\text{কারণ} \ln\left(\frac{a}{b}\right)=\ln a-\ln b]$\\$=\log_5e\lim_{h\to0}\frac{\ln\left(1+\frac{h}{x}\right)}{h}$\\$=\log_5e\lim_{h\to0}\frac{1}{h}\left(\frac{h}{x}-\frac{1}{2}\frac{h^2}{x^2}+\frac{1}{3}\frac{h^3}{x^3}\cdots\right)$\\$=\log_5e\lim_{h\to0}\left(\frac{1}{x}-\frac{1}{2}\frac{h}{x^2}+\frac{1}{3}\frac{h^2}{x^3}\cdots\right)$\\$=\log_5e\cdot\frac{1}{x}$\\$\therefore \frac{d}{dx}(\log_5x)=\frac{1}{x}\log_5e\ (Ans.)$

**Final answer:** $\frac{1}{x}\log_5e$

## ID 1116

**Question:** $\frac{d}{dp}(e^{-2p})$

**Solution:** $(xxi)$ ধরি, $f(p)=e^{-2p}$\\$\therefore f(p+h)=e^{-2(p+h)}=e^{-2p-2h}$\\সংজ্ঞানুসারে আমরা পাই,\\$\frac{d}{dp}\{f(p)\}=\lim_{h\to0}\frac{f(p+h)-f(p)}{h}$\\$\therefore \frac{d}{dp}(e^{-2p})=\lim_{h\to0}\frac{e^{-2p-2h}-e^{-2p}}{h}$\\$=\lim_{h\to0}\frac{e^{-2p}(e^{-2h}-1)}{h}$\\$=\lim_{h\to0}e^{-2p}\left\{\frac{1-\frac{2h}{1!}+\frac{(-2h)^2}{2!}+\cdots-1}{h}\right\}$\\$=\lim_{h\to0}e^{-2p}(-2+2h+h \text{এর উচ্চ অনন্তরিক পদসমূহ})$\\$=-2e^{-2p}\ (Ans.)$

**Final answer:** $-2e^{-2p}$

## ID 1117

**Question:** $\frac{d}{dx}(\cosec3x)$

**Solution:** $(xxii)$ প্রদত্ত ফাংশন $=\frac{1}{\sin3x}=\cosec3x$\\$\text{ধরি,} g(x)=\cosec3x$\\$\therefore g(x+h)=\cosec3(x+h)$\\মূল নিয়মের সাহায্যে অন্তরক সহগ হতে পাই,\\$\frac{d}{dx}\{g(x)\}=\lim_{h\to0}\frac{g(x+h)-g(x)}{h}$\\$\therefore \frac{d}{dx}(\cosec3x)=\lim_{h\to0}\frac{\cosec3(x+h)-\cosec3x}{h}$\\$=\lim_{h\to0}\frac{\frac{1}{\sin3(x+h)}-\frac{1}{\sin3x}}{h}$\\$=\lim_{h\to0}\frac{\sin3x-\sin(3x+3h)}{h\sin(3x+3h)\sin3x}$\\$=\lim_{h\to0}\frac{2\cos\frac{3x+3x+3h}{2}\sin\frac{3x-3x-3h}{2}}{h\cdot\sin(3x+3h)\sin3x}$\\$=\lim_{h\to0}\frac{2\cos\left(3x+\frac{3h}{2}\right)\sin\left(-\frac{3h}{2}\right)}{h\cdot\sin(3x+3h)\sin3x}$\\$=-3\lim_{h\to0}\frac{\sin\frac{3h}{2}}{\frac{3h}{2}}\lim_{h\to0}\frac{\cos\left(3x+\frac{3h}{2}\right)}{\sin(3x+3h)\sin3x}$\\$=-3\cdot1\cdot\frac{\cos3x}{\sin3x\cdot\sin3x}=-3\cot3x\cosec3x\ (Ans.)$

**Final answer:** $-3\cot3x\cosec3x$

## ID 1118

**Question:** $\frac{d}{dx}\left(\frac{\ln x}{\cos x}\right)$

**Solution:** $(xxiii)$ ধরি, $f(x)=\frac{\ln x}{\cos x}$ $\therefore f(x+h)=\frac{\ln(x+h)}{\cos(x+h)}$\\মূল নিয়মের সাহায্যে অন্তরক সহগ হতে পাই,\\$\frac{d}{dx}\{f(x)\}=\lim_{h\to0}\frac{f(x+h)-f(x)}{h}$\\$\therefore \frac{d}{dx}\left(\frac{\ln x}{\cos x}\right)=\lim_{h\to0}\frac{1}{h}\left[\frac{\ln(x+h)}{\cos(x+h)}-\frac{\ln x}{\cos x}\right]$\\$=\lim_{h\to0}\frac{1}{h}\left[\frac{\ln(x+h)\cos x-\cos(x+h)\ln x}{\cos(x+h)\cos x}\right]$\\$=\lim_{h\to0}\frac{1}{h\cos(x+h)\cos x}\{\ln(x+h)\cos x-\cos x\ln x+\cos x\ln x-\cos(x+h)\ln x\}$\\$=\frac{1}{\cos(x+0)\cos x}\left[\cos x\lim_{h\to0}\frac{1}{h}\left\{\ln(x+h)-\ln x\right\}-\ln x\lim_{h\to0}\frac{1}{h}\{\cos(x+h)-\cos x\}\right]$\\$=\frac{1}{\cos^2x}\left[\cos x\lim_{h\to0}\frac{1}{h}\ln\frac{x+h}{x}-\ln x\lim_{h\to0}\frac{1}{h}\left\{2\sin\frac{(2x+h)}{2}\sin\frac{(-h)}{2}\right\}\right]$\\$=\frac{1}{\cos^2x}\left[\cos x\lim_{h\to0}\frac{1}{h}\ln\left(1+\frac{h}{x}\right)-\ln x\left\{-\lim_{h\to0}\sin\frac{1}{2}(2x+h)\cdot\frac{\sin(h/2)}{h/2}\right\}\right]$\\$=\frac{1}{\cos^2x}\left[\cos x\lim_{h\to0}\left(\frac{1}{x}-\frac{1}{2}\frac{h}{x^2}+\frac{1}{3}\frac{h^2}{x^3}-\cdots\right)+\sin x\ln x\right]$\\$=\frac{1}{\cos^2x}\left[\frac{1}{x}\cos x+\sin x\ln x\right]\ (Ans.)$

**Final answer:** $\frac{1}{\cos^2x}\left[\frac{1}{x}\cos x+\sin x\ln x\right]$

## ID 1119

**Question:** $\frac{d}{dx}\left(\frac{3x+5}{2x^2-9}\right)$

**Solution:** $4.(i)\ \frac{d}{dx}\left(\frac{3x+5}{2x^2-9}\right)$\\$=\frac{(2x^2-9)\frac{d}{dx}(3x+5)-(3x+5)\frac{d}{dx}(2x^2-9)}{(2x^2-9)^2}$\\$=\frac{3(2x^2-9)-4x(3x+5)}{4x^4-36x^2+81}=\frac{6x^2-27-12x^2-20x}{4x^4-36x^2+81}$\\$=\frac{-(6x^2+20x+27)}{4x^4-36x^2+81}\ (Ans.)$

**Final answer:** $\frac{-(6x^2+20x+27)}{4x^4-36x^2+81}$

## ID 1120

**Question:** $\frac{d}{dx}\left(\frac{\sqrt{x}+1}{\sqrt{x}-1}\right)$

**Solution:** $(ii)\ \frac{d}{dx}\left(\frac{\sqrt{x}+1}{\sqrt{x}-1}\right)$\\$=\frac{(\sqrt{x}-1)\frac{d}{dx}(\sqrt{x}+1)-(\sqrt{x}+1)\frac{d}{dx}(\sqrt{x}-1)}{(\sqrt{x}-1)^2}$\\$=\frac{(\sqrt{x}-1)\frac{1}{2\sqrt{x}}-(\sqrt{x}+1)\frac{1}{2\sqrt{x}}}{(\sqrt{x}-1)^2}$\\$=\frac{\frac{1}{2\sqrt{x}}\{(\sqrt{x}-1)-(\sqrt{x}+1)\}}{(\sqrt{x}-1)^2}$\\$=\frac{\frac{1}{2\sqrt{x}}(\sqrt{x}-1-\sqrt{x}-1)}{(\sqrt{x}-1)^2}=\frac{\frac{1}{2\sqrt{x}}(-2)}{(\sqrt{x}-1)^2}$\\$=\frac{-\frac{1}{\sqrt{x}}}{(\sqrt{x}-1)^2}=\frac{-1}{\sqrt{x}(\sqrt{x}-1)^2}\ (Ans.)$

**Final answer:** $\frac{-1}{\sqrt{x}(\sqrt{x}-1)^2}$

## ID 1121

**Question:** $\frac{d}{dx}\left(\frac{x^2+1}{x^2+3}\right)$

**Solution:** $(iii)\ \frac{d}{dx}\left(\frac{x^2+1}{x^2+3}\right)=\frac{(x^2+3)\frac{d}{dx}(x^2+1)-(x^2+1)\frac{d}{dx}(x^2+3)}{(x^2+3)^2}$\\$=\frac{2x(x^2+3)-2x(x^2+1)}{(x^2+3)^2}=\frac{2x(x^2+3-x^2-1)}{(x^2+3)^2}=\frac{4x}{(x^2+3)^2}\ (Ans.)$

**Final answer:** $\frac{4x}{(x^2+3)^2}$

## ID 1122

**Question:** $\frac{d}{dt}\left(\frac{1+t+t^2}{1-t+t^2}\right)$

**Solution:** $(iv)\ \frac{d}{dt}\left(\frac{1+t+t^2}{1-t+t^2}\right)$\\$=\frac{(1-t+t^2)\frac{d}{dt}(1+t+t^2)-(1+t+t^2)\frac{d}{dt}(1-t+t^2)}{(1-t+t^2)^2}$\\$=\frac{(1-t+t^2)(2t+1)-(1+t+t^2)(2t-1)}{(1-t+t^2)^2}$\\$=\frac{2t-2t^2+2t^3+1-t+t^2-2t-2t^2-2t^3+1+t+t^2}{(1-t+t^2)^2}$\\$=\frac{2-2t^2}{(1-t+t^2)^2}=\frac{2(1-t^2)}{(1-t+t^2)^2}\ (Ans.)$

**Final answer:** $\frac{2(1-t^2)}{(1-t+t^2)^2}$

## ID 1123

**Question:** $\frac{d}{dx}\left(\frac{1+\sin x}{1+\cos x}\right)$

**Solution:** $(v)\ \frac{d}{dx}\left(\frac{1+\sin x}{1+\cos x}\right)$\\$=\frac{(1+\cos x)\frac{d}{dx}(1+\sin x)-(1+\sin x)\frac{d}{dx}(1+\cos x)}{(1+\cos x)^2}$\\$=\frac{(1+\cos x)\cos x-(1+\sin x)(-\sin x)}{(1+\cos x)^2}$\\$=\frac{\cos x+\cos^2x+\sin x+\sin^2x}{(1+\cos x)^2}$\\$=\frac{1+\sin x+\cos x}{(1+\cos x)^2}\quad [\text{কারণ} \sin^2\theta+\cos^2\theta=1]$\\$\therefore \frac{d}{dx}\left(\frac{1+\sin x}{1+\cos x}\right)=\frac{1+\sin x+\cos x}{(1+\cos x)^2}\ (Ans.)$

**Final answer:** $\frac{1+\sin x+\cos x}{(1+\cos x)^2}$

## ID 1124

**Question:** $\frac{d}{dx}\left(\frac{\cos x}{1+\sin^2x}\right)$

**Solution:** $(vii)\ \frac{d}{dx}\left(\frac{\cos x}{1+\sin^2x}\right)=\frac{(1+\sin^2x)\frac{d}{dx}(\cos x)-\cos x\frac{d}{dx}(1+\sin^2x)}{(1+\sin^2x)^2}$\\$=\frac{(1+\sin^2x)(-\sin x)-\cos x(2\sin x\cos x)}{(1+\sin^2x)^2}$\\$=\frac{-\sin x(1+\sin^2x+2\cos^2x)}{(1+\sin^2x)^2}=\frac{-\sin x(2+\cos^2x)}{(1+\sin^2x)^2}\ (Ans.)$

**Final answer:** $\frac{-\sin x(2+\cos^2x)}{(1+\sin^2x)^2}$

## ID 1125

**Question:** $\frac{d}{dx}\left(\frac{\sin x}{x^2+\cos x}\right)$

**Solution:** $(viii)\ \frac{d}{dx}\left(\frac{\sin x}{x^2+\cos x}\right)$\\$=\frac{(x^2+\cos x)\frac{d}{dx}(\sin x)-\sin x\frac{d}{dx}(x^2+\cos x)}{(x^2+\cos x)^2}$\\$=\frac{(x^2+\cos x)(\cos x)-\sin x(2x-\sin x)}{(x^2+\cos x)^2}$\\$=\frac{x^2\cos x+\cos^2x-2x\sin x+\sin^2x}{(x^2+\cos x)^2}$\\$=\frac{x^2\cos x-2x\sin x+1}{(x^2+\cos x)^2}\ (Ans.)$

**Final answer:** $\frac{x^2\cos x-2x\sin x+1}{(x^2+\cos x)^2}$

## ID 1126

**Question:** $\frac{d}{dx}\left(\frac{x\sin x}{1+\cos x}\right)$

**Solution:** $(ix)\ \frac{d}{dx}\left(\frac{x\sin x}{1+\cos x}\right)$\\$=\frac{(1+\cos x)\frac{d}{dx}(x\sin x)-x\sin x\frac{d}{dx}(1+\cos x)}{(1+\cos x)^2}$\\$=\frac{(1+\cos x)(\sin x+x\cos x)-x\sin x\cdot(-\sin x)}{(1+\cos x)^2}$\\$=\frac{\sin x+\sin x\cos x+x\cos x+x(\cos^2x+\sin^2x)}{(1+\cos x)^2}$\\$=\frac{\sin x+\sin x\cos x+x\cos x+x}{(1+\cos x)^2}$\\$=\frac{\cos x(x+\sin x)+1(x+\sin x)}{(1+\cos x)^2}=\frac{(x+\sin x)(1+\cos x)}{(1+\cos x)^2}=\frac{x+\sin x}{1+\cos x}\ (Ans.)$

**Final answer:** $\frac{x+\sin x}{1+\cos x}$

## ID 1127

**Question:** $\frac{d}{dx}\left(\frac{\tan x+\cot x}{3e^x}\right)$

**Solution:** $(x)\ \frac{d}{dx}\left(\frac{\tan x+\cot x}{3e^x}\right)$\\$=\frac{3e^x\frac{d}{dx}(\tan x+\cot x)-(\tan x+\cot x)\frac{d}{dx}(3e^x)}{(3e^x)^2}$\\$=\frac{3e^x(\sec^2x-\cosec^2x)-3e^x(\tan x+\cot x)}{(3e^x)^2}$\\$=\frac{(1+\tan^2x)-1-\cot^2x-\tan x-\cot x}{3e^x}$\\$=\frac{(\tan x+\cot x)(\tan x-\cot x)-(\tan x+\cot x)}{3e^x}$\\$=\frac{(\tan x+\cot x)(\tan x-\cot x-1)}{3e^x}\ (Ans.)$

**Final answer:** $\frac{(\tan x+\cot x)(\tan x-\cot x-1)}{3e^x}$

## ID 1128

**Question:** $\frac{d}{d\theta}\left(\frac{\cos\theta-\sin\theta}{\cos\theta+\sin\theta}\right)$

**Solution:** $(xi)\ \frac{d}{d\theta}\left(\frac{\cos\theta-\sin\theta}{\cos\theta+\sin\theta}\right)$\\$=\frac{d}{d\theta}\left(\frac{1-\frac{\sin\theta}{\cos\theta}}{1+\frac{\sin\theta}{\cos\theta}}\right)=\frac{d}{d\theta}\left(\frac{1-\tan\theta}{1+\tan\theta}\right)$\\$=\frac{(1+\tan\theta)\frac{d}{d\theta}(1-\tan\theta)-(1-\tan\theta)\frac{d}{d\theta}(1+\tan\theta)}{(1+\tan\theta)^2}$\\$=\frac{(1+\tan\theta)(-\sec^2\theta)-(1-\tan\theta)\sec^2\theta}{(1+\tan\theta)^2}$\\$=\frac{-\sec^2\theta-\sec^2\theta\tan\theta-\sec^2\theta+\sec^2\theta\tan\theta}{(1+\tan\theta)^2}$\\$=\frac{-2\sec^2\theta}{(1+\tan\theta)^2}\ (Ans.)$

**Final answer:** $\frac{-2\sec^2\theta}{(1+\tan\theta)^2}$

## ID 1129

**Question:** $\frac{d}{dx}\left(\frac{x^4}{\ln x}\right)$

**Solution:** $(xiii)\ \frac{d}{dx}\left(\frac{x^4}{\ln x}\right)=\frac{\ln x\frac{d}{dx}(x^4)-x^4\frac{d}{dx}(\ln x)}{(\ln x)^2}$\\$=\frac{\ln x(4x^3)-x^4\cdot\frac{1}{x}}{(\ln x)^2}=\frac{x^3(4\ln x-1)}{(\ln x)^2}\ (Ans.)$

**Final answer:** $\frac{x^3(4\ln x-1)}{(\ln x)^2}$

## ID 1130

**Question:** $\frac{d}{dx}(x^2\ln x)$

**Solution:** $5.(i)\ \frac{d}{dx}(x^2\ln x)=x^2\frac{d}{dx}(\ln x)+\ln x\frac{d}{dx}(x^2)$\\$=\frac{x^2}{x}+2x\ln x=x+2x\ln x$\\$=x(1+2\ln x)\ (Ans.)$

**Final answer:** $x(1+2\ln x)$

## ID 1131

**Question:** $\frac{d}{dx}(x^4e^x)$

**Solution:** $(ii)\ \frac{d}{dx}(x^4e^x)=x^4\frac{d}{dx}(e^x)+e^x\frac{d}{dx}(x^4)$\\$=e^xx^4+4x^3e^x=x^3e^x(x+4)\ (Ans.)$

**Final answer:** $x^3e^x(x+4)$

## ID 1132

**Question:** $\frac{d}{dx}(x^5\log_ax)$

**Solution:** $(iii)\ \frac{d}{dx}(x^5\log_ax)=\frac{d}{dx}(x^5\log_ae\log_ex)$\\$=\log_ae\frac{d}{dx}(x^5\cdot\log_ex)$\\$=\log_ae\left[x^5\cdot\frac{1}{x}+\log_ex\cdot5x^4\right]$\\$=x^4(\log_ae+5\log_ae\cdot\log_ex)$\\$=x^4(\log_ae+5\log_ax)\ (Ans.)$

**Final answer:** $x^4(\log_ae+5\log_ax)$

## ID 1133

**Question:** $\frac{d}{dx}(5e^x\log_ax)$

**Solution:** $(iv)\ \frac{d}{dx}(5e^x\log_ax)=\frac{d}{dx}\{5e^x\cdot\log_ae\cdot\ln(x)\}$\\$=5\log_ae\frac{d}{dx}\{e^x\ln(x)\}$\\$=5\log_ae\left[\ln(x)e^x+e^x\frac{1}{x}\right]$\\$=5e^x\left\{\log_ae\cdot\ln(x)+\frac{1}{x}\log_ae\right\}$\\$=5e^x\left(\log_ax+\frac{1}{x}\log_ae\right)\ (Ans.)$

**Final answer:** $5e^x\left(\log_ax+\frac{1}{x}\log_ae\right)$

## ID 1134

**Question:** $\frac{d}{dx}(e^x\log_ax)$

**Solution:** $(v)\ \frac{d}{dx}(e^x\log_ax)=e^x\frac{d}{dx}(\log_ax)+\log_ax\frac{d}{dx}(e^x)$\\$=e^x\frac{d}{dx}(\ln x\log_ae)+\log_ax\cdot e^x$\\$=\frac{e^x}{x}\log_ae+e^x\log_ax$\\$=e^x\left(\frac{1}{x}\log_ae+\log_ax\right)\ (Ans.)$

**Final answer:** $e^x\left(\frac{1}{x}\log_ae+\log_ax\right)$

## ID 1135

**Question:** $\frac{d}{dx}(e^x\sin x)$

**Solution:** $(vi)\ \frac{d}{dx}(e^x\sin x)=e^x\frac{d}{dx}(\sin x)+\sin x\frac{d}{dx}(e^x)$\\$=e^x(\cos x+\sin x)\ (Ans.)$

**Final answer:** $e^x(\cos x+\sin x)$

## ID 1136

**Question:** $\frac{d}{dx}(e^x\cos x)$

**Solution:** $(vii)\ \frac{d}{dx}(e^x\cos x)=e^x\frac{d}{dx}(\cos x)+\cos x\frac{d}{dx}(e^x)$\\$=-e^x\sin x+e^x\cos x$\\$=e^x(\cos x-\sin x)\ (Ans.)$

**Final answer:** $e^x(\cos x-\sin x)$

## ID 1137

**Question:** $\frac{d}{dx}(x^2\cos x)$

**Solution:** $(viii)\ \frac{d}{dx}(x^2\cos x)=x^2\frac{d}{dx}(\cos x)+\cos x\frac{d}{dx}(x^2)$\\$=-x^2\sin x+2x\cos x$\\$=x(2\cos x-x\sin x)\ (Ans.)$

**Final answer:** $x(2\cos x-x\sin x)$

## ID 1138

**Question:** $\frac{d}{dx}(x^3\tan x)$

**Solution:** $(ix)\ \frac{d}{dx}(x^3\tan x)=x^3\frac{d}{dx}(\tan x)+\tan x\frac{d}{dx}(x^3)$\\$=x^3\sec^2x+3x^2\tan x$\\$=x^2(x\sec^2x+3\tan x)\ (Ans.)$

**Final answer:** $x^2(x\sec^2x+3\tan x)$

## ID 1139

**Question:** $\frac{d}{dx}\{(\log_ax)(\ln x)\}$

**Solution:** $(x)\ \frac{d}{dx}\{(\log_ax)(\ln x)\}$\\$=\log_ax\cdot\frac{d}{dx}(\ln x)+(\ln x)\frac{d}{dx}(\log_ax)$\\$=\log_ax\cdot\frac{1}{x}+\ln x\cdot\frac{1}{x}\log_ae$\\$=\frac{1}{x}(\log_ax+\log_ae\ln x)\ (Ans.)$

**Final answer:** $\frac{1}{x}(\log_ax+\log_ae\ln x)$

## ID 1140

**Question:** $\frac{d}{dx}(\sqrt[3]{x}\sin x)$

**Solution:** $(xi)\ \frac{d}{dx}(\sqrt[3]{x}\sin x)=\frac{d}{dx}(x^{\frac{1}{3}}\sin x)$\\$=x^{\frac{1}{3}}\frac{d}{dx}(\sin x)+\sin x\frac{d}{dx}(x^{\frac{1}{3}})$\\$=x^{\frac{1}{3}}\cos x+\frac{1}{3}x^{\frac{1}{3}-1}\sin x$\\$=x^{\frac{1}{3}}\cos x+\frac{\sin x}{3x^{\frac{2}{3}}}=x^{\frac{1}{3}}\left(\cos x+\frac{\sin x}{3x}\right)\ (Ans.)$

**Final answer:** $x^{\frac{1}{3}}\left(\cos x+\frac{\sin x}{3x}\right)$

## ID 1141

**Question:** $\frac{d}{dx}(\sin x\cos x)$

**Solution:** $(xiii)\ \frac{d}{dx}(\sin x\cos x)=\frac{1}{2}\frac{d}{dx}(2\sin x\cos x)$\\$=\frac{1}{2}\frac{d}{dx}(\sin2x)=\frac{1}{2}\cos2x\cdot2=\cos2x\ (Ans.)$

**Final answer:** $\cos2x$

## ID 1142

**Question:** $\frac{d}{dx}(x^2e^x\ln x)$

**Solution:** $(xiv)\ \frac{d}{dx}(x^2e^x\ln x)=x^2\frac{d}{dx}(e^x\ln x)+e^x\ln x\frac{d}{dx}(x^2)$\\$=x^2\left\{e^x\frac{d}{dx}(\ln x)+\ln x\frac{d}{dx}(e^x)\right\}+e^x\ln x\cdot2x$\\$=x^2e^x\cdot\frac{1}{x}+x^2e^x\ln x+2xe^x\ln x$\\$=xe^x(2\ln x+x\ln x+1)\ (Ans.)$

**Final answer:** $xe^x(2\ln x+x\ln x+1)$

## ID 1143

**Question:** $\frac{d}{dx}(\sqrt[3]{3x^2+1})$

**Solution:** $1.(i)\ \frac{d}{dx}(\sqrt[3]{3x^2+1})=\frac{d}{dx}(3x^2+1)^{\frac{1}{3}}$\\$=\frac{1}{3}(3x^2+1)^{\frac{1}{3}-1}\cdot\frac{d}{dx}(3x^2+1)$\\$=\frac{1}{3}(3x^2+1)^{-\frac{2}{3}}\cdot6x=2x(3x^2+1)^{-\frac{2}{3}}\ (Ans.)$

**Final answer:** $2x(3x^2+1)^{-\frac{2}{3}}$

## ID 1144

**Question:** $\frac{d}{dx}\left(\frac{1}{\sqrt[3]{4-3x}}\right)$

**Solution:** $(ii)\ \frac{d}{dx}\left(\frac{1}{\sqrt[3]{4-3x}}\right)=\frac{d}{dx}(4-3x)^{-\frac{1}{3}}$\\$=-\frac{1}{3}(4-3x)^{-\frac{1}{3}-1}\cdot(-3)$\\$=(4-3x)^{-\frac{4}{3}}=\frac{1}{(4-3x)^{\frac{4}{3}}}\ (Ans.)$

**Final answer:** $\frac{1}{(4-3x)^{\frac{4}{3}}}$

## ID 1145

**Question:** $\frac{d}{dx}(\sqrt{ax^2+bx+c})$

**Solution:** $(iii)\ \frac{d}{dx}(\sqrt{ax^2+bx+c})$\\$=\frac{1}{2\sqrt{ax^2+bx+c}}(2ax+b)$\\$=\frac{2ax+b}{2\sqrt{ax^2+bx+c}}\ (Ans.)$

**Final answer:** $\frac{2ax+b}{2\sqrt{ax^2+bx+c}}$

## ID 1146

**Question:** $\frac{d}{d\theta}\left(\sin\frac{\theta}{2}+\cos5\theta\right)$

**Solution:** $(iv)\ \frac{d}{d\theta}\left(\sin\frac{\theta}{2}+\cos5\theta\right)=\cos\frac{\theta}{2}\frac{d}{d\theta}\left(\frac{\theta}{2}\right)-\sin5\theta\frac{d}{d\theta}(5\theta)$\\$=\frac{1}{2}\cos\frac{\theta}{2}-5\sin5\theta\ (Ans.)$

**Final answer:** $\frac{1}{2}\cos\frac{\theta}{2}-5\sin5\theta$

## ID 1147

**Question:** $\frac{d}{d\theta}(\cos^4\theta)$

**Solution:** $(v)\ \frac{d}{d\theta}(\cos^4\theta)=4\cos^3\theta\frac{d}{d\theta}(\cos\theta)$\\$=-4\cos^3\theta\sin\theta\ (Ans.)$

**Final answer:** $-4\cos^3\theta\sin\theta$

## ID 1148

**Question:** $\frac{d}{dx}(\sec\sqrt{x})$

**Solution:** $(vi)\ \frac{d}{dx}(\sec\sqrt{x})=\sec\sqrt{x}\tan\sqrt{x}\cdot\frac{d}{dx}(\sqrt{x})$\\$=\frac{1}{2\sqrt{x}}\sec\sqrt{x}\tan\sqrt{x}\ (Ans.)$

**Final answer:** $\frac{1}{2\sqrt{x}}\sec\sqrt{x}\tan\sqrt{x}$

## ID 1149

**Question:** $\frac{d}{d\theta}(\sqrt{\tan\theta})$

**Solution:** $(vii)\ \frac{d}{d\theta}(\sqrt{\tan\theta})=\frac{1}{2}(\tan\theta)^{\frac{1}{2}-1}\cdot\frac{d}{d\theta}(\tan\theta)$\\$=\frac{1}{2\sqrt{\tan\theta}}\sec^2\theta=\frac{\sec^2\theta}{2\sqrt{\tan\theta}}\ (Ans.)$

**Final answer:** $\frac{\sec^2\theta}{2\sqrt{\tan\theta}}$

## ID 1150

**Question:** $\frac{d}{dx}(\sqrt{\tan e^{x^2}})$

**Solution:** $(viii)\ \frac{d}{dx}(\sqrt{\tan e^{x^2}})=\frac{d}{dx}\{\tan e^{x^2}\}^{\frac{1}{2}}$\\$=\frac{1}{2}(\tan e^{x^2})^{-\frac{1}{2}}\cdot\frac{d}{dx}(\tan e^{x^2})$\\$=\frac{1}{2}\cdot\frac{1}{\sqrt{\tan e^{x^2}}}\cdot\sec^2e^{x^2}\cdot\frac{d}{dx}(e^{x^2})$\\$=\frac{x e^{x^2}\sec^2e^{x^2}}{\sqrt{\tan e^{x^2}}}\ (Ans.)$

**Final answer:** $\frac{x e^{x^2}\sec^2e^{x^2}}{\sqrt{\tan e^{x^2}}}$

## ID 1151

**Question:** $\frac{d}{dx}(\cos x^\circ)$

**Solution:** $(ix)$ যদি, $y=\cos x^\circ$\\$\therefore y=\cos\frac{\pi x}{180}\quad[\text{কারণ} 1^\circ=\frac{\pi}{180}\ \text{radian}]$\\$\therefore\frac{dy}{dx}=-\sin\frac{\pi x}{180}\cdot\frac{\pi}{180}=-\frac{\pi}{180}\sin\frac{\pi x}{180}\ (Ans.)$

**Final answer:** $-\frac{\pi}{180}\sin\frac{\pi x}{180}$

## ID 1152

**Question:** $\frac{d}{dx}(\cos^2x^2)$

**Solution:** $(x)\ \frac{d}{dx}(\cos^2x^2)=2\cos x^2\cdot\frac{d}{dx}(\cos x^2)$\\$=2\cos x^2\cdot(-\sin x^2)\frac{d}{dx}(x^2)$\\$=-4x\cos x^2\sin x^2=-2x(2\sin x^2\cos x^2)$\\$=-2x\sin2x^2\ (Ans.)$

**Final answer:** $-2x\sin2x^2$

## ID 1153

**Question:** $\frac{d}{dx}(\sin^3x^3)$

**Solution:** $(xi)\ \frac{d}{dx}(\sin^3x^3)=\frac{d}{dx}(\sin x^3)^3=3(\sin x^3)^2\frac{d}{dx}(\sin x^3)$\\$=3\sin^2x^3\cos x^3\frac{d}{dx}(x^3)=9x^2\sin^2x^3\cos x^3\ (Ans.)$

**Final answer:** $9x^2\sin^2x^3\cos x^3$

## ID 1154

**Question:** $\frac{d}{dx}(e^{\sqrt{x}})$

**Solution:** $2.(i)\ \frac{d}{dx}(e^{\sqrt{x}})=e^{\sqrt{x}}\frac{d}{dx}(\sqrt{x})$\\$=\frac{e^{\sqrt{x}}}{2\sqrt{x}}\ (Ans.)$

**Final answer:** $\frac{e^{\sqrt{x}}}{2\sqrt{x}}$

## ID 1155

**Question:** $\frac{d}{dx}\left(\sqrt{\frac{1}{e^x}}\right)$

**Solution:** $(ii)\ \frac{d}{dx}\left(\sqrt{\frac{1}{e^x}}\right)=\frac{d}{dx}(e^{-x})^{\frac{1}{2}}$\\$=\frac{1}{2}(e^{-x})^{\frac{1}{2}-1}\cdot\frac{d}{dx}(e^{-x})$\\$=\frac{1}{2\sqrt{e^{-x}}}e^{-x}(-1)=-\frac{1}{2\sqrt{e^x}}\ (Ans.)$

**Final answer:** $-\frac{1}{2\sqrt{e^x}}$

## ID 1156

**Question:** $\frac{d}{dx}(\sqrt{e^{\sqrt{x}}})$

**Solution:** $(iii)\ \frac{d}{dx}(\sqrt{e^{\sqrt{x}}})=\frac{1}{2\sqrt{e^{\sqrt{x}}}}\cdot\frac{d}{dx}(e^{\sqrt{x}})$\\$=\frac{1}{2\sqrt{e^{\sqrt{x}}}}e^{\sqrt{x}}\frac{d}{dx}(\sqrt{x})$\\$=\frac{e^{\sqrt{x}}}{4\sqrt{x}\sqrt{e^{\sqrt{x}}}}\ (Ans.)$

**Final answer:** $\frac{e^{\sqrt{x}}}{4\sqrt{x}\sqrt{e^{\sqrt{x}}}}$

## ID 1157

**Question:** $\frac{d}{dx}(e^{\sin\sqrt{x}})$

**Solution:** $(iv)\ \frac{d}{dx}(e^{\sin\sqrt{x}})=e^{\sin\sqrt{x}}\frac{d}{dx}(\sin\sqrt{x})$\\$=e^{\sin\sqrt{x}}\cos\sqrt{x}\frac{d}{dx}(\sqrt{x})=\frac{\cos\sqrt{x}\,e^{\sin\sqrt{x}}}{2\sqrt{x}}\ (Ans.)$

**Final answer:** $\frac{\cos\sqrt{x}\,e^{\sin\sqrt{x}}}{2\sqrt{x}}$

## ID 1158

**Question:** $\frac{d}{dx}(e^{\sin2x})$

**Solution:** $(v)$ যদি, $y=e^{\sin2x}$\\$\therefore\frac{dy}{dx}=e^{\sin2x}\cdot2\cos2x=2\cos2x\,e^{\sin2x}\ (Ans.)$

**Final answer:** $2\cos2x\,e^{\sin2x}$

## ID 1159

**Question:** $\frac{d}{dx}(e^{\sin(\cos^{-1}2x)})$

**Solution:** $(vi)\ \frac{d}{dx}e^{\sin(\cos^{-1}2x)}$\\$=e^{\sin(\cos^{-1}2x)}\cos(\cos^{-1}2x)\cdot\frac{-1}{\sqrt{1-4x^2}}\cdot2$\\$=\frac{-4x}{\sqrt{1-4x^2}}e^{\sin(\cos^{-1}2x)}\ (Ans.)$

**Final answer:** $\frac{-4x}{\sqrt{1-4x^2}}e^{\sin(\cos^{-1}2x)}$

## ID 1160

**Question:** $\frac{d}{dx}(e^x\log2xe^{2x})$

**Solution:** $(vii)$ দেওয়া আছে, $f(x)=e^x$\\$\therefore f'(x)=e^x$\\$\therefore\frac{d}{dx}\{f'(x)\log2x\,f(2x)\}=\frac{d}{dx}(e^x\log2x\,e^{2x})$\\$=\frac{d}{dx}(e^{3x}\log2x)=e^{3x}\frac{d}{dx}(\log2x)+\log2x\frac{d}{dx}(e^{3x})$\\$=e^{3x}\cdot\frac{1}{2x}\cdot2+\log2x\cdot3e^{3x}=\frac{e^{3x}}{x}+3e^{3x}\log2x\ (Ans.)$

**Final answer:** $\frac{e^{3x}}{x}+3e^{3x}\log2x$

## ID 1161

**Question:** $\frac{d}{d\theta}\{\ln(\cos2\theta)\}$

**Solution:** $3.(i)\ \frac{d}{d\theta}\{\ln(\cos2\theta)\}=\frac{1}{\cos2\theta}\frac{d}{d\theta}(\cos2\theta)$\\$=\frac{-\sin2\theta}{\cos2\theta}\frac{d}{d\theta}(2\theta)=-2\tan2\theta\ (Ans.)$

**Final answer:** $-2\tan2\theta$

## ID 1162

**Question:** $\frac{d}{dx}\{\ln(\sin2x)\}$

**Solution:** $(ii)$ যদি, $y=\ln(\sin2x)$\\$\therefore\frac{dy}{dx}=\frac{1}{\sin2x}\frac{d}{dx}(\sin2x)=\frac{2\cos2x}{\sin2x}=2\cot2x\ (Ans.)$

**Final answer:** $2\cot2x$

## ID 1163

**Question:** $\frac{d}{dx}(\ln\sqrt{x})$

**Solution:** $(iii)\ \frac{d}{dx}(\ln\sqrt{x})=\frac{1}{\sqrt{x}}\frac{d}{dx}(\sqrt{x})$\\$=\frac{1}{2\sqrt{x}\sqrt{x}}=\frac{1}{2x}\ (Ans.)$

**Final answer:** $\frac{1}{2x}$

## ID 1164

**Question:** $\frac{d}{dx}(\ln x)^2$

**Solution:** $(iv)\ \frac{d}{dx}(\ln x)^2=2\ln x\cdot\frac{d}{dx}(\ln x)$\\$=\frac{2\ln x}{x}\ (Ans.)$

**Final answer:** $\frac{2\ln x}{x}$

## ID 1165

**Question:** $\frac{d}{dx}(\log_{10}x)$

**Solution:** $(v)$ মনে করি, $y=\log_{10}x$\\$\therefore y=\log_ex\times\log_{10}e$\\$\therefore\frac{dy}{dx}=\log_{10}e\frac{d}{dx}(\log_ex)=\frac{1}{x}\log_{10}e\ (Ans.)$

**Final answer:** $\frac{1}{x}\log_{10}e$

## ID 1166

**Question:** $\frac{d}{dx}(\log_3 3x)$

**Solution:** $(vi)\ \frac{d}{dx}(\log_3 3x)=\frac{d}{dx}(\log_e3x\times\log_3e)$\\$=\log_3e\frac{d}{dx}(\log_e3x)=\log_3e\cdot\frac{1}{3x}\frac{d}{dx}(3x)$\\$=\log_3e\cdot\frac{1}{3x}\cdot3=\frac{1}{x}\log_3e\ (Ans.)$

**Final answer:** $\frac{1}{x}\log_3e$

## ID 1167

**Question:** $\frac{d}{dx}\{\ln(ax^2+bx+c)\}$

**Solution:** $(vii)\ \frac{d}{dx}\{\ln(ax^2+bx+c)\}$\\$=\frac{1}{ax^2+bx+c}\frac{d}{dx}(ax^2+bx+c)=\frac{2ax+b}{ax^2+bx+c}\ (Ans.)$

**Final answer:** $\frac{2ax+b}{ax^2+bx+c}$

## ID 1168

**Question:** $\frac{d}{dx}(10^{\ln(\sin x)})$

**Solution:** $(viii)\ \frac{d}{dx}(10^{\ln\sin x})=10^{\ln\sin x}\ln10\frac{d}{dx}(\ln\sin x)$\\$=10^{\ln\sin x}\ln10\cdot\frac{1}{\sin x}\frac{d}{dx}(\sin x)$\\$=10^{\ln\sin x}\ln10\cot x\ (Ans.)$

**Final answer:** $10^{\ln\sin x}\ln10\cot x$

## ID 1169

**Question:** $\frac{d}{dx}(e^{2\ln(\tan5x)})$

**Solution:** $4.(i)$ যদি, $y=e^{2\ln(\tan5x)}$\\$\text{বা,} y=e^{\ln(\tan5x)^2},\quad y=(\tan5x)^2$\\$\therefore\frac{dy}{dx}=2\tan5x\frac{d}{dx}(\tan5x)=2\tan5x\sec^2 5x\cdot5$\\$\therefore\frac{dy}{dx}=10\tan5x\sec^2 5x\ (Ans.)$

**Final answer:** $10\tan5x\sec^2 5x$

## ID 1170

**Question:** $\frac{d}{dx}(e^{5\ln(\tan5x)})$

**Solution:** $(ii)$ যদি, $y=e^{5\ln\tan5x}=e^{\ln(\tan5x)^5}=(\tan5x)^5$\\$\therefore\frac{dy}{dx}=5\tan^4 5x\frac{d}{dx}(\tan5x)=5\tan^4 5x\sec^2 5x\cdot5$\\$=25(\tan5x)^4\sec^2 5x\ (Ans.)$

**Final answer:** $25(\tan5x)^4\sec^2 5x$

## ID 1171

**Question:** $\frac{d}{dx}\{\cos(\ln x)+\ln(\tan x)\}$

**Solution:** $(iii)$ যদি, $y=\cos(\ln x)+\ln(\tan x)$\\$\therefore\frac{dy}{dx}=-\sin(\ln x)\cdot\frac{1}{x}+\frac{1}{\tan x}\sec^2x$\\$=-\frac{1}{x}\sin(\ln x)+\frac{\cos x}{\sin x}\cdot\frac{1}{\cos^2x}$\\$=-\frac{1}{x}\sin(\ln x)+\frac{1}{\sin x\cos x}$\\$=-\frac{1}{x}\sin(\ln x)+\frac{2}{\sin2x}=2\cosec2x-\frac{1}{x}\sin(\ln x)\ (Ans.)$

**Final answer:** $2\cosec2x-\frac{1}{x}\sin(\ln x)$

## ID 1172

**Question:** $\frac{d}{dx}(1+\sin2x)^2$

**Solution:** $(iv)\ \frac{d}{dx}(1+\sin2x)^2=2(1+\sin2x)\frac{d}{dx}(1+\sin2x)$\\$=2(1+\sin2x)\cos2x\frac{d}{dx}(2x)=4\cos2x(1+\sin2x)\ (Ans.)$

**Final answer:** $4\cos2x(1+\sin2x)$

## ID 1173

**Question:** $\frac{d}{dx}\left[\sin^2\{\ln(\sec x)\}\right]$

**Solution:** $5.(i)\ \frac{d}{dx}\left[\sin^2\{\ln(\sec x)\}\right]$\\$=2\sin\{\ln(\sec x)\}\cdot\frac{d}{dx}\sin\{\ln(\sec x)\}$\\$=2\sin\{\ln(\sec x)\}\cos\{\ln(\sec x)\}\cdot\frac{d}{dx}\{\ln(\sec x)\}$\\$=\sin\{2\ln(\sec x)\}\cdot\frac{1}{\sec x}\cdot\sec x\tan x$\\$=\tan x\sin\{2\ln(\sec x)\}\ (Ans.)$

**Final answer:** $\tan x\sin\{2\ln(\sec x)\}$

## ID 1174

**Question:** $\frac{d}{dx}\left[\sin^2(\ln\cos x)\right]$

**Solution:** $(ii)$ যদি, $y=\sin^2(\ln\cos x)$\\$\therefore\frac{dy}{dx}=2\sin(\ln\cos x)\frac{d}{dx}\{\sin(\ln\cos x)\}$\\$=2\sin(\ln\cos x)\cos(\ln\cos x)\frac{d}{dx}\{\ln(\cos x)\}$\\$=\sin\{2\ln(\cos x)\}\cdot\frac{1}{\cos x}(-\sin x)$\\$=-\tan x\sin\{2\ln(\cos x)\}\ (Ans.)$

**Final answer:** $-\tan x\sin\{2\ln(\cos x)\}$

## ID 1175

**Question:** $\frac{d}{dx}\{\ln(\sin x^2)\}$

**Solution:** $(iii)\ \frac{d}{dx}\{\ln(\sin x^2)\}=\frac{1}{\sin x^2}\cdot\frac{d}{dx}(\sin x^2)$\\$=\frac{\cos x^2}{\sin x^2}\cdot\frac{d}{dx}(x^2)=2x\cot x^2\ (Ans.)$

**Final answer:** $2x\cot x^2$

## ID 1176

**Question:** $\frac{d}{dx}\left[\{\ln(\sin x^2)\}^n\right]$

**Solution:** $(iv)$ মনে করি, $y=\{\ln(\sin x^2)\}^n$\\$\therefore\frac{dy}{dx}=n\{\ln(\sin x^2)\}^{n-1}\frac{d}{dx}\{\ln(\sin x^2)\}$\\$=n\{\ln(\sin x^2)\}^{n-1}\cdot\frac{1}{\sin x^2}\cos x^2\cdot2x$\\$=2nx\cot x^2\{\ln(\sin x^2)\}^{n-1}\ (Ans.)$

**Final answer:** $2nx\cot x^2\{\ln(\sin x^2)\}^{n-1}$

## ID 1177

**Question:** $\frac{d}{dx}\left[\sin^2\{\ln(x^2)\}\right]$

**Solution:** $(v)\ \frac{d}{dx}\left[\sin^2\{\ln(x^2)\}\right]$\\$=\frac{d}{dx}\left[\sin\{\ln(x^2)\}\right]^2$\\$=2\sin\{\ln(x^2)\}\cos\{\ln(x^2)\}\frac{d}{dx}\{\ln(x^2)\}$\\$=\sin\{2\ln(x^2)\}\cdot\frac{1}{x^2}\cdot2x$\\$=\frac{2\sin\{2\ln(x^2)\}}{x}=\frac{2\sin(4\ln x)}{x}\ (Ans.)$

**Final answer:** $\frac{2\sin(4\ln x)}{x}$

## ID 1178

**Question:** $\frac{d}{dx}\left[\sin\{\ln(\sec x)\}\right]$

**Solution:** $(vi)\ \frac{d}{dx}\left[\sin\{\ln(\sec x)\}\right]=\cos\{\ln(\sec x)\}\frac{d}{dx}\{\ln(\sec x)\}$\\$=\cos\{\ln(\sec x)\}\cdot\frac{1}{\sec x}\frac{d}{dx}(\sec x)$\\$=\cos\{\ln(\sec x)\}\cdot\frac{1}{\sec x}\sec x\tan x$\\$=\tan x\cos\{\ln(\sec x)\}\ (Ans.)$

**Final answer:** $\tan x\cos\{\ln(\sec x)\}$

## ID 1179

**Question:** $\frac{d}{dx}(x^\circ\cos x^\circ)$

**Solution:** $6.(i)\ \frac{d}{dx}(x^\circ\cos x^\circ)$\\$=\frac{d}{dx}\left(\frac{\pi x}{180}\cos\frac{\pi x}{180}\right)\quad[\text{কারণ} x^\circ=\frac{\pi x}{180}]$\\$=\frac{\pi x}{180}\frac{d}{dx}\left(\cos\frac{\pi x}{180}\right)+\cos\frac{\pi x}{180}\frac{d}{dx}\left(\frac{\pi x}{180}\right)$\\$=-\frac{\pi x}{180}\sin\frac{\pi x}{180}\cdot\frac{\pi}{180}+\frac{\pi}{180}\cos\frac{\pi x}{180}$\\$=\frac{\pi}{180}\left(\cos\frac{\pi x}{180}-\frac{\pi x}{180}\sin\frac{\pi x}{180}\right)\ (Ans.)$

**Final answer:** $\frac{\pi}{180}\left(\cos\frac{\pi x}{180}-\frac{\pi x}{180}\sin\frac{\pi x}{180}\right)$

## ID 1180

**Question:** $\frac{d}{d\theta}(\theta^\circ\sin\theta^\circ)$

**Solution:** $(ii)\ \frac{d}{d\theta}(\theta^\circ\sin\theta^\circ)$\\$=\frac{d}{d\theta}\left(\frac{\theta\pi}{180}\sin\frac{\theta\pi}{180}\right)\quad[\text{কারণ} \theta^\circ=\frac{\theta\pi}{180}]$\\$=\frac{\theta\pi}{180}\frac{d}{d\theta}\left(\sin\frac{\theta\pi}{180}\right)+\sin\frac{\theta\pi}{180}\frac{d}{d\theta}\left(\frac{\theta\pi}{180}\right)$\\$=\frac{\theta\pi}{180}\cos\frac{\theta\pi}{180}\cdot\frac{\pi}{180}+\sin\frac{\theta\pi}{180}\cdot\frac{\pi}{180}$\\$=\frac{\pi}{180}\left(\frac{\theta\pi}{180}\cos\frac{\theta\pi}{180}+\sin\frac{\theta\pi}{180}\right)\ (Ans.)$

**Final answer:** $\frac{\pi}{180}\left(\frac{\theta\pi}{180}\cos\frac{\theta\pi}{180}+\sin\frac{\theta\pi}{180}\right)$

## ID 1181

**Question:** $\frac{d}{dx}\left(x\sqrt{x^2+a^2}\right)$

**Solution:** $(iii)\ \frac{d}{dx}\left(x\sqrt{x^2+a^2}\right)=x\frac{d}{dx}(x^2+a^2)^{\frac{1}{2}}+\sqrt{x^2+a^2}\frac{d}{dx}(x)$\\$=x\frac{2x}{2\sqrt{x^2+a^2}}+\sqrt{x^2+a^2}$\\$=\frac{x^2}{\sqrt{x^2+a^2}}+\sqrt{x^2+a^2}=\frac{2x^2+a^2}{\sqrt{x^2+a^2}}\ (Ans.)$

**Final answer:** $\frac{2x^2+a^2}{\sqrt{x^2+a^2}}$

## ID 1182

**Question:** $\frac{d}{dx}(x\sqrt{\sin x})$

**Solution:** $(iv)\ \frac{d}{dx}(x\sqrt{\sin x})=\sqrt{\sin x}\frac{d}{dx}(x)+x\frac{d}{dx}(\sqrt{\sin x})$\\$=\sqrt{\sin x}+x\cdot\frac{1}{2\sqrt{\sin x}}\frac{d}{dx}(\sin x)$\\$=\sqrt{\sin x}+\frac{x\cos x}{2\sqrt{\sin x}}\ (Ans.)$

**Final answer:** $\sqrt{\sin x}+\frac{x\cos x}{2\sqrt{\sin x}}$

## ID 1183

**Question:** $\frac{d}{dx}(x^n\ln2x)$

**Solution:** $(v)\ \frac{d}{dx}(x^n\ln2x)=x^n\frac{d}{dx}(\ln2x)+\ln(2x)\frac{d}{dx}(x^n)$\\$=x^n\cdot\frac{1}{2x}\cdot2+\ln(2x)\cdot nx^{n-1}$\\$=x^{n-1}+nx^{n-1}\ln(2x)=x^{n-1}\{1+n\ln(2x)\}\ (Ans.)$

**Final answer:** $x^{n-1}\{1+n\ln(2x)\}$

## ID 1184

**Question:** $\frac{d}{dx}\left[\sin(e^{\sqrt{1-x}})\right]$

**Solution:** $(vi)\ \frac{d}{dx}\left[\sin(e^{\sqrt{1-x}})\right]=\cos(e^{\sqrt{1-x}})\frac{d}{dx}e^{\sqrt{1-x}}$\\$=\cos(e^{\sqrt{1-x}})e^{\sqrt{1-x}}\frac{d}{dx}\sqrt{1-x}$\\$=e^{\sqrt{1-x}}\cos e^{\sqrt{1-x}}\cdot\frac{-1}{2\sqrt{1-x}}\frac{d}{dx}(1-x)$\\$=-\frac{e^{\sqrt{1-x}}\cos e^{\sqrt{1-x}}}{2\sqrt{1-x}}\ (Ans.)$

**Final answer:** $-\frac{e^{\sqrt{1-x}}\cos e^{\sqrt{1-x}}}{2\sqrt{1-x}}$

## ID 1185

**Question:** $\frac{d}{dx}(e^{ax}\tan^2x)$

**Solution:** $(vii)\ \frac{d}{dx}(e^{ax}\tan^2x)$\\$=e^{ax}\frac{d}{dx}(\tan^2x)+\tan^2x\frac{d}{dx}(e^{ax})$\\$=e^{ax}\cdot2\tan x\frac{d}{dx}(\tan x)+\tan^2x\cdot e^{ax}\frac{d}{dx}(ax)$\\$=e^{ax}\cdot2\tan x\sec^2x+ae^{ax}\tan^2x$\\$=e^{ax}\tan x(2\sec^2x+a\tan x)\ (Ans.)$

**Final answer:** $e^{ax}\tan x(2\sec^2x+a\tan x)$

## ID 1186

**Question:** $\frac{d}{dx}\left(2^x\ln\frac{1}{1-x}\right)$

**Solution:** $(viii)$ যদি, $y=2^x\ln\frac{1}{1-x}=2^x\ln(1-x)^{-1}$\\$=-2^x\ln(1-x)$\\$\therefore\frac{dy}{dx}=-\left[2^x\frac{d}{dx}\{\ln(1-x)\}+\ln(1-x)\frac{d}{dx}(2^x)\right]$\\$=-\left[2^x\frac{1}{1-x}(-1)+\ln(1-x)2^x\ln2\right]$\\$=\frac{2^x}{1-x}+2^x\ln2\ln\frac{1}{1-x}\ (Ans.)$

**Final answer:** $\frac{2^x}{1-x}+2^x\ln2\ln\frac{1}{1-x}$

## ID 1187

**Question:** $\frac{d}{dx}\left(\frac{\ln(\cos x)}{x}\right)$

**Solution:** $7.(i)$ যদি, $y=\frac{\ln(\cos x)}{x}$\\$\therefore\frac{dy}{dx}=\frac{x\frac{d}{dx}\{\ln(\cos x)\}-\ln(\cos x)\frac{d}{dx}(x)}{x^2}$\\$=\frac{x\cdot\frac{1}{\cos x}(-\sin x)-\ln(\cos x)\cdot1}{x^2}$\\$=\frac{-x\tan x-\ln(\cos x)}{x^2}\ (Ans.)$

**Final answer:** $\frac{-x\tan x-\ln(\cos x)}{x^2}$

## ID 1188

**Question:** $\frac{d}{dx}\sqrt{\frac{1+\cos x}{1-\cos x}}$

**Solution:** $(ii)\ \frac{d}{dx}\left(\sqrt{\frac{1+\cos x}{1-\cos x}}\right)=\frac{d}{dx}\left(\sqrt{\frac{2\cos^2\frac{x}{2}}{2\sin^2\frac{x}{2}}}\right)$\\$=\frac{d}{dx}\left(\cot\frac{x}{2}\right)=-\cosec^2\frac{x}{2}\frac{d}{dx}\left(\frac{x}{2}\right)$\\$=-\frac{\cosec^2\frac{x}{2}}{2}=-\frac{1}{2\sin^2\frac{x}{2}}=-\frac{1}{1-\cos x}\ (Ans.)$

**Final answer:** $-\frac{1}{1-\cos x}$

## ID 1189

**Question:** $\frac{d}{dx}\left(\frac{\sin2x}{1+\cos2x}\right)^2$

**Solution:** $(iii)$ যদি, $y=\left(\frac{\sin2x}{1+\cos2x}\right)^2=\left(\frac{2\sin x\cos x}{2\cos^2x}\right)^2$\\$\therefore y=\tan^2x$\\$\therefore\frac{dy}{dx}=\frac{d}{dx}(\tan^2x)=2\tan x\sec^2x\ (Ans.)$

**Final answer:** $2\tan x\sec^2x$

## ID 1190

**Question:** $\frac{d}{dx}\left(\frac{\tan x-\cot x}{\tan x+\cot x}\right)$

**Solution:** $(iv)$ যদি, $y=\frac{\tan x-\cot x}{\tan x+\cot x}$\\$=\frac{\frac{\sin x}{\cos x}-\frac{\cos x}{\sin x}}{\frac{\sin x}{\cos x}+\frac{\cos x}{\sin x}}=\frac{\sin^2x-\cos^2x}{\sin^2x+\cos^2x}$\\$=\sin^2x-\cos^2x=-\cos2x$\\$\therefore\frac{dy}{dx}=-(-\sin2x)2=2\sin2x\ (Ans.)$

**Final answer:** $2\sin2x$

## ID 1191

**Question:** $\frac{d}{dx}\left(\frac{e^x+\ln x}{\log_ax}\right)$

**Solution:** $(v)\ \frac{d}{dx}\left(\frac{e^x+\ln x}{\log_ax}\right)$\\$=\frac{\log_ax\frac{d}{dx}(e^x+\ln x)-(e^x+\ln x)\frac{d}{dx}(\log_ax)}{(\log_ax)^2}$\\$=\frac{\log_ax\left(e^x+\frac{1}{x}\right)-(e^x+\ln x)\frac{1}{x}\log_ae}{(\log_ax)^2}\ (Ans.)$

**Final answer:** $\frac{\log_ax\left(e^x+\frac{1}{x}\right)-(e^x+\ln x)\frac{1}{x}\log_ae}{(\log_ax)^2}$

## ID 1192

**Question:** $\frac{d}{dx}\{x^3\sin(\ln x)\}$

**Solution:** $(vi)\ \frac{d}{dx}\{x^3\sin(\ln x)\}$\\$=x^3\frac{d}{dx}\{\sin(\ln x)\}+\sin(\ln x)\frac{d}{dx}(x^3)$\\$=x^3\cos(\ln x)\cdot\frac{1}{x}+\sin(\ln x)\cdot3x^2$\\$=x^2\{\cos(\ln x)+3\sin(\ln x)\}\ (Ans.)$

**Final answer:** $x^2\{\cos(\ln x)+3\sin(\ln x)\}$

## ID 1193

**Question:** $\frac{d}{dx}\left[\sin^2\{(\ln x)^2\}\right]$

**Solution:** $(vii)\ \frac{d}{dx}\left[\sin^2\{(\ln x)^2\}\right]=2\sin\{(\ln x)^2\}\frac{d}{dx}\left[\sin\{(\ln x)^2\}\right]$\\$=2\sin\{(\ln x)^2\}\cos\{(\ln x)^2\}\frac{d}{dx}\{(\ln x)^2\}$\\$=\sin\{2(\ln x)^2\}\cdot2\ln x\frac{d}{dx}(\ln x)$\\$=\frac{2\ln x}{x}\sin\{2(\ln x)^2\}\ (Ans.)$

**Final answer:** $\frac{2\ln x}{x}\sin\{2(\ln x)^2\}$

## ID 1194

**Question:** $y=\frac{x\ln x}{\sqrt{1+x^2}}$

**Solution:** $(viii)$ যদি, $y=\frac{x\ln x}{\sqrt{1+x^2}}$\\$\therefore\frac{dy}{dx}=\frac{\sqrt{1+x^2}\frac{d}{dx}(x\ln x)-x\ln x\frac{d}{dx}(\sqrt{1+x^2})}{(\sqrt{1+x^2})^2}$\\$=\frac{\sqrt{1+x^2}\left(x\cdot\frac{1}{x}+\ln x\right)-x\ln x\frac{1}{2}(1+x^2)^{-\frac{1}{2}}2x}{1+x^2}$\\$=\frac{(1+x^2)(1+\ln x)-x^2\ln x}{(1+x^2)\sqrt{1+x^2}}$\\$=\frac{1+x^2+\ln x}{(\sqrt{1+x^2})^3}\ (Ans.)$

**Final answer:** $\frac{1+x^2+\ln x}{(\sqrt{1+x^2})^3}$

## ID 1195

**Question:** $\frac{d}{dx}(\tan^{-1}\sqrt{x})$

**Solution:** $8.(i)\ \frac{d}{dx}(\tan^{-1}\sqrt{x})=\frac{1}{1+(\sqrt{x})^2}\frac{d}{dx}(\sqrt{x})$\\$=\frac{1}{2\sqrt{x}(1+x)}\ (Ans.)$

**Final answer:** $\frac{1}{2\sqrt{x}(1+x)}$

## ID 1196

**Question:** $\frac{d}{dx}\cos^{-1}(1-2x)$

**Solution:** $(ii)\ \frac{d}{dx}\cos^{-1}(1-2x)=\frac{-1}{\sqrt{1-(1-2x)^2}}\frac{d}{dx}(1-2x)$\\$=\frac{2}{\sqrt{1-1+4x-4x^2}}=\frac{1}{\sqrt{x-x^2}}\ (Ans.)$

**Final answer:** $\frac{1}{\sqrt{x-x^2}}$

## ID 1197

**Question:** $\frac{d}{dx}\left(\sin^{-1}(\sin\sqrt{x})\right)$

**Solution:** $(iii)\ \frac{d}{dx}\left(\sin^{-1}(\sin\sqrt{x})\right)=\frac{d}{dx}\{\sin^{-1}\sin\sqrt{x}\}$\\$=\frac{d}{dx}\sqrt{x}=\frac{1}{2}x^{-\frac{1}{2}}=\frac{1}{2\sqrt{x}}\ (Ans.)$

**Final answer:** $\frac{1}{2\sqrt{x}}$

## ID 1198

**Question:** $\frac{d}{dx}(3^{\sin^{-1}x})$

**Solution:** $(iv)\ \frac{d}{dx}(3^{\sin^{-1}x})=3^{\sin^{-1}x}\ln3\frac{d}{dx}(\sin^{-1}x)$\\$=\frac{3^{\sin^{-1}x}\ln3}{\sqrt{1-x^2}}\ (Ans.)$

**Final answer:** $\frac{3^{\sin^{-1}x}\ln3}{\sqrt{1-x^2}}$

## ID 1199

**Question:** $\frac{d}{dx}(\sec^{-1}x)^2$

**Solution:** $(v)\ \frac{d}{dx}(\sec^{-1}x)^2=2\sec^{-1}x\frac{d}{dx}(\sec^{-1}x)$\\$=\frac{2\sec^{-1}x}{x\sqrt{x^2-1}}\ (Ans.)$

**Final answer:** $\frac{2\sec^{-1}x}{x\sqrt{x^2-1}}$

## ID 1200

**Question:** $\frac{d}{dx}\tan^{-1}(\sec x+\tan x)$

**Solution:** $(vi)\ \frac{d}{dx}\{\tan^{-1}(\sec x+\tan x)\}$\\$=\frac{1}{1+(\sec x+\tan x)^2}\frac{d}{dx}(\sec x+\tan x)$\\$=\frac{\sec x\tan x+\sec^2x}{\sec^2x+\sec^2x+2\sec x\tan x}$\\$=\frac{\sec x\tan x+\sec^2x}{2(\sec^2x+\sec x\tan x)}=\frac{1}{2}\ (Ans.)$

**Final answer:** $\frac{1}{2}$

## ID 1201

**Question:** $\frac{d}{dx}\tan^{-1}(\sin e^x)$

**Solution:** $(vii)$ মনে করি, $y=\tan^{-1}(\sin e^x)$\\$\therefore\frac{dy}{dx}=\frac{1}{1+\sin^2e^x}\cdot\frac{d}{dx}(\sin e^x)$\\$=\frac{1}{1+\sin^2e^x}\cos e^x\cdot e^x=\frac{e^x\cos e^x}{1+\sin^2e^x}\ (Ans.)$

**Final answer:** $\frac{e^x\cos e^x}{1+\sin^2e^x}$

## ID 1202

**Question:** $\frac{d}{dx}\sin^{-1}(\sqrt{xe^x})$

**Solution:** $(viii)$ যদি, $y=\sin^{-1}(\sqrt{xe^x})$\\$\therefore\frac{dy}{dx}=\frac{1}{\sqrt{1-xe^x}}\cdot\frac{d}{dx}(\sqrt{xe^x})$\\$=\frac{1}{\sqrt{1-xe^x}}\cdot\frac{xe^x+e^x}{2\sqrt{xe^x}}=\frac{(x+1)e^x}{2\sqrt{xe^x}\sqrt{1-xe^x}}\ (Ans.)$

**Final answer:** $\frac{(x+1)e^x}{2\sqrt{xe^x}\sqrt{1-xe^x}}$

## ID 1203

**Question:** $\frac{d}{dx}\sin^{-1}(\sin e^x)$

**Solution:** $(ix)$ $y=\sin^{-1}(\sin e^x)$। $\sin^{-1}$-এর প্রধান মানের পরিসর $[-\frac{\pi}{2},\frac{\pi}{2}]$। তাই যে অন্তরালে $0<e^x\le\frac{\pi}{2}$, অর্থাৎ $x\le\ln\frac{\pi}{2}$, সেখানে $\sin^{-1}(\sin e^x)=e^x$।\\সুতরাং ঐ অন্তরালে $\frac{dy}{dx}=\frac{d}{dx}(e^x)=e^x$। সাধারণভাবে প্রধান শাখার বাইরে ফলটি শাখাভেদে piecewise হবে।

**Final answer:** $e^x$; যেখানে $0<e^x\le\frac{\pi}{2}$

## ID 1204

**Question:** $\frac{d}{dx}(\tan x\sin^{-1}x)$

**Solution:** $(x)\ \frac{d}{dx}(\tan x\sin^{-1}x)$\\$=\tan x\frac{d}{dx}(\sin^{-1}x)+\sin^{-1}x\frac{d}{dx}(\tan x)$\\$=\tan x\frac{1}{\sqrt{1-x^2}}+\sin^{-1}x\sec^2x\ (Ans.)$

**Final answer:** $\frac{\tan x}{\sqrt{1-x^2}}+\sin^{-1}x\sec^2x$

## ID 1205

**Question:** $\frac{d}{dx}\left\{\tan^{-1}\left(\frac{\cos x}{1+\sin x}\right)\right\}$

**Solution:** $(xi)\ \frac{d}{dx}\left\{\tan^{-1}\left(\frac{\cos x}{1+\sin x}\right)\right\}$\\$=\frac{1}{1+\frac{\cos^2x}{(1+\sin x)^2}}\frac{d}{dx}\left(\frac{\cos x}{1+\sin x}\right)$\\$=\frac{(1+\sin x)^2}{(1+\sin x)^2+\cos^2x}\cdot\frac{(1+\sin x)(-\sin x)-\cos x\cos x}{(1+\sin x)^2}$\\$=\frac{-\sin x-\sin^2x-\cos^2x}{2+2\sin x}=-\frac{1+\sin x}{2(1+\sin x)}=-\frac{1}{2}\ (Ans.)$

**Final answer:** $-\frac{1}{2}$

## ID 1206

**Question:** $\frac{d}{dx}(e^x\sin^{-1}x)$

**Solution:** $(xii)\ \frac{d}{dx}\{e^x\sin^{-1}x\}=\sin^{-1}x\frac{d}{dx}(e^x)+e^x\frac{d}{dx}(\sin^{-1}x)$\\$=e^x\sin^{-1}x+\frac{e^x}{\sqrt{1-x^2}}\ (Ans.)$

**Final answer:** $e^x\sin^{-1}x+\frac{e^x}{\sqrt{1-x^2}}$

## ID 1207

**Question:** $\frac{d}{dx}\{(x^2+1)\tan^{-1}x-x\}$

**Solution:** $(xiii)$ যদি, $y=(x^2+1)\tan^{-1}x-x$\\$\therefore\frac{dy}{dx}=(x^2+1)\frac{d}{dx}(\tan^{-1}x)+\tan^{-1}x\frac{d}{dx}(x^2+1)-\frac{d}{dx}(x)$\\$=(x^2+1)\frac{1}{1+x^2}+\tan^{-1}x\cdot2x-1$\\$=1+2x\tan^{-1}x-1=2x\tan^{-1}x\ (Ans.)$

**Final answer:** $2x\tan^{-1}x$

## ID 1208

**Question:** $\frac{d}{dx}\left\{2\tan^{-1}\sqrt{\frac{x-a}{b-x}}\right\}$

**Solution:** $(xiv)$ যদি, $y=2\tan^{-1}\sqrt{\frac{x-a}{b-x}}$\\$=\cos^{-1}\frac{1-\frac{x-a}{b-x}}{1+\frac{x-a}{b-x}}=\cos^{-1}\frac{b+a-2x}{b-a}$\\$\therefore\frac{dy}{dx}=\frac{-1}{\sqrt{1-\left(\frac{b+a-2x}{b-a}\right)^2}}\frac{d}{dx}\left(\frac{b+a-2x}{b-a}\right)$\\$=\frac{1}{\sqrt{(b-x)(x-a)}}\ (Ans.)$

**Final answer:** $\frac{1}{\sqrt{(b-x)(x-a)}}$

## ID 1209

**Question:** $\frac{d}{dx}\left\{\tan^{-1}\left(\frac{x^2}{e^x}\right)+\tan^{-1}\left(\frac{e^x}{x^2}\right)\right\}$

**Solution:** $(xv)$ যদি, $y=\tan^{-1}\left(\frac{x^2}{e^x}\right)+\tan^{-1}\left(\frac{e^x}{x^2}\right)$\\$=\tan^{-1}\left(\frac{x^2}{e^x}\right)+\cot^{-1}\left(\frac{x^2}{e^x}\right)=\frac{\pi}{2}$\\$\therefore\frac{dy}{dx}=0\ (Ans.)$

**Final answer:** $0$

## ID 1210

**Question:** $\frac{d}{dx}\left(\sin^{-1}\frac{2x}{1+x^2}\right)$

**Solution:** $9.(i)\ \frac{d}{dx}\left(\sin^{-1}\frac{2x}{1+x^2}\right)=\frac{d}{dx}(2\tan^{-1}x)$\\$=\frac{2}{1+x^2}\ (Ans.)$

**Final answer:** $\frac{2}{1+x^2}$

## ID 1211

**Question:** $\frac{d}{dx}\sec^{-1}\left(\frac{1+x^2}{1-x^2}\right)$

**Solution:** $(ii)$ মনে করি, $y=\sec^{-1}\left(\frac{1+x^2}{1-x^2}\right)$\\$\therefore y=\cos^{-1}\frac{1-x^2}{1+x^2}=2\tan^{-1}x$\\$\therefore\frac{dy}{dx}=2\cdot\frac{1}{1+x^2}=\frac{2}{1+x^2}\ (Ans.)$

**Final answer:** $\frac{2}{1+x^2}$

## ID 1212

**Question:** $\frac{d}{dx}\tan^{-1}\frac{2\sqrt{x}}{1-x}$

**Solution:** $(iii)$ যদি, $y=\tan^{-1}\frac{2\sqrt{x}}{1-x}=2\tan^{-1}\sqrt{x}$\\$\therefore\frac{dy}{dx}=2\frac{d}{dx}(\tan^{-1}\sqrt{x})=2\frac{1}{1+(\sqrt{x})^2}\frac{d}{dx}(\sqrt{x})$\\$=\frac{2}{1+x}\cdot\frac{1}{2}x^{-\frac{1}{2}}=\frac{1}{(1+x)\sqrt{x}}\ (Ans.)$

**Final answer:** $\frac{1}{(1+x)\sqrt{x}}$

## ID 1213

**Question:** $\frac{d}{dx}\tan^{-1}\frac{6\sqrt{x}}{1-9x}$

**Solution:** $(iv)$ যদি, $y=\tan^{-1}\frac{6\sqrt{x}}{1-9x}=\tan^{-1}\frac{2\cdot3\sqrt{x}}{1-(3\sqrt{x})^2}$\\$\text{বা,} y=2\tan^{-1}(3\sqrt{x})$\\$\therefore\frac{dy}{dx}=2\frac{1}{1+9x}\cdot3\frac{1}{2\sqrt{x}}$\\$\therefore\frac{dy}{dx}=\frac{3}{\sqrt{x}(1+9x)}\ (Ans.)$

**Final answer:** $\frac{3}{\sqrt{x}(1+9x)}$

## ID 1214

**Question:** $\frac{d}{dx}\tan^{-1}\frac{4x}{1-4x^2}$

**Solution:** $(v)\ \frac{d}{dx}\tan^{-1}\left(\frac{4x}{1-4x^2}\right)=\frac{d}{dx}\left\{\tan^{-1}\frac{2\cdot2x}{1-(2x)^2}\right\}$\\$=\frac{d}{dx}(2\tan^{-1}2x)=2\frac{1}{1+(2x)^2}\cdot2=\frac{4}{1+4x^2}\ (Ans.)$

**Final answer:** $\frac{4}{1+4x^2}$

## ID 1215

**Question:** $\frac{d}{dx}\tan^{-1}\frac{x}{\sqrt{1-x^2}}$

**Solution:** $(vi)$ যদি, $y=\tan^{-1}\frac{x}{\sqrt{1-x^2}}$\\$\text{ধরি,} x=\sin\theta\quad\therefore\theta=\sin^{-1}x$\\$\therefore y=\tan^{-1}\left(\frac{\sin\theta}{\sqrt{1-\sin^2\theta}}\right)=\tan^{-1}\left(\frac{\sin\theta}{\cos\theta}\right)$\\$=\tan^{-1}(\tan\theta)=\theta=\sin^{-1}x$\\$\therefore\frac{dy}{dx}=\frac{1}{\sqrt{1-x^2}}\ (Ans.)$

**Final answer:** $\frac{1}{\sqrt{1-x^2}}$

## ID 1216

**Question:** $\frac{d}{dx}\tan^{-1}\left(\frac{1-\sqrt{x}}{1+\sqrt{x}}\right)$

**Solution:** $(vii)$ যদি, $y=\tan^{-1}\left(\frac{1-\sqrt{x}}{1+\sqrt{x}}\right)$\\$=\tan^{-1}\left(\frac{1-\tan\sqrt{x}}{1+\tan\sqrt{x}}\right)=\tan^{-1}\tan\frac{\pi}{4}-\tan^{-1}\sqrt{x}$\\$=\frac{\pi}{4}-\tan^{-1}\sqrt{x}$\\$\therefore\frac{dy}{dx}=-\frac{1}{1+(\sqrt{x})^2}\frac{d}{dx}(\sqrt{x})=-\frac{1}{2\sqrt{x}(1+x)}\ (Ans.)$

**Final answer:** $-\frac{1}{2\sqrt{x}(1+x)}$

## ID 1217

**Question:** $\frac{d}{dx}\tan^{-1}\sqrt{\frac{1-x}{1+x}}$

**Solution:** $(viii)$ যদি, $y=\tan^{-1}\sqrt{\frac{1-x}{1+x}}$\\$\therefore y=\tan^{-1}\sqrt{\frac{1-\cos\theta}{1+\cos\theta}}\quad[\text{ধরি,} x=\cos\theta]$\\$=\tan^{-1}\sqrt{\frac{2\sin^2\frac{\theta}{2}}{2\cos^2\frac{\theta}{2}}}=\tan^{-1}\tan\frac{\theta}{2}=\frac{\theta}{2}$\\$\therefore y=\frac{1}{2}\cos^{-1}x$\\$\therefore\frac{d}{dx}\left(\tan^{-1}\sqrt{\frac{1-x}{1+x}}\right)=-\frac{1}{2\sqrt{1-x^2}}\ (Ans.)$

**Final answer:** $-\frac{1}{2\sqrt{1-x^2}}$

## ID 1218

**Question:** $\frac{d}{dx}\tan^{-1}\frac{1}{\sqrt{x^2-1}}$

**Solution:** $(ix)$ যদি, $y=\tan^{-1}\frac{1}{\sqrt{x^2-1}}$\\মনে করি, $x=\sec\theta,\ \theta=\sec^{-1}x$\\$\therefore y=\tan^{-1}\frac{1}{\sqrt{\sec^2\theta-1}}=\tan^{-1}\frac{1}{\sqrt{\tan^2\theta}}$\\$=\tan^{-1}\frac{1}{\tan\theta}=\tan^{-1}\cot\theta=\tan^{-1}\tan\left(\frac{\pi}{2}-\theta\right)$\\$=\frac{\pi}{2}-\theta$\\$\therefore y=\frac{\pi}{2}-\sec^{-1}x$\\$\frac{dy}{dx}=\frac{d}{dx}\left(\frac{\pi}{2}\right)-\frac{d}{dx}(\sec^{-1}x)=0-\frac{1}{x\sqrt{x^2-1}}=-\frac{1}{x\sqrt{x^2-1}}\ (Ans.)$

**Final answer:** $-\frac{1}{x\sqrt{x^2-1}}$

## ID 1219

**Question:** $\frac{d}{dx}\left[\cos^{-1}\left\{\left(\frac{1+x}{2}\right)^{\frac{1}{2}}\right\}\right]$

**Solution:** $(x)$ যদি, $y=\cos^{-1}\left\{\left(\frac{1+x}{2}\right)^{\frac{1}{2}}\right\}$\\$\text{ধরি,} x=\cos\theta,\ \theta=\cos^{-1}x$\\$\therefore y=\cos^{-1}\sqrt{\frac{1+\cos\theta}{2}}=\cos^{-1}\sqrt{\cos^2\frac{\theta}{2}}=\cos^{-1}\cos\frac{\theta}{2}=\frac{\theta}{2}$\\$\therefore y=\frac{1}{2}\cos^{-1}x$\\$\therefore\frac{dy}{dx}=\frac{1}{2}\frac{d}{dx}(\cos^{-1}x)=-\frac{1}{2\sqrt{1-x^2}}\ (Ans.)$

**Final answer:** $-\frac{1}{2\sqrt{1-x^2}}$

## ID 1220

**Question:** $\frac{d}{dx}\left[\sin^{-1}\{2x\sqrt{1-x^2}\}\right]$

**Solution:** $(xi)$ ধরি, $x=\sin\theta,\ \theta=\sin^{-1}x$\\$\therefore y=\sin^{-1}\{2x\sqrt{1-x^2}\}=\sin^{-1}\{2\sin\theta\sqrt{1-\sin^2\theta}\}$\\$=\sin^{-1}(2\sin\theta\cos\theta)=\sin^{-1}(\sin2\theta)=2\theta=2\sin^{-1}x$\\$\therefore\frac{d}{dx}\left[\sin^{-1}\{2x\sqrt{1-x^2}\}\right]=\frac{d}{dx}(2\sin^{-1}x)=\frac{2}{\sqrt{1-x^2}}\ (Ans.)$

**Final answer:** $\frac{2}{\sqrt{1-x^2}}$

## ID 1221

**Question:** $\frac{d}{dx}\left[\sin^{-1}\{2ax\sqrt{1-a^2x^2}\}\right]$

**Solution:** $(xii)$ যদি, $y=\sin^{-1}\{2ax\sqrt{1-a^2x^2}\}$\\ধরি, $ax=\sin\theta$\\$\therefore y=\sin^{-1}\{2\sin\theta\sqrt{1-\sin^2\theta}\}=\sin^{-1}\sin2\theta=2\theta$\\$\therefore y=2\sin^{-1}(ax)$\\$\therefore\frac{dy}{dx}=2\frac{d}{dx}\{\sin^{-1}(ax)\}=\frac{2a}{\sqrt{1-a^2x^2}}\ (Ans.)$

**Final answer:** $\frac{2a}{\sqrt{1-a^2x^2}}$

## ID 1222

**Question:** $\frac{d}{dx}\left[\sin^{-1}(3x-4x^3)\right]$

**Solution:** $(xiii)$ মনে করি, $y=\sin^{-1}(3x-4x^3)$\\$y=\sin^{-1}(3\sin\theta-4\sin^3\theta)\quad[\text{ধরি,} x=\sin\theta]$\\$=\sin^{-1}\sin3\theta=3\theta=3\sin^{-1}x$\\$\therefore\frac{dy}{dx}=\frac{3}{\sqrt{1-x^2}}\ (Ans.)$

**Final answer:** $\frac{3}{\sqrt{1-x^2}}$

## ID 1223

**Question:** $\frac{d}{dx}\left[\cos^{-1}(4x^3-3x)\right]$

**Solution:** $(xiv)$ মনে করি, $y=\cos^{-1}(4x^3-3x)$\\$y=\cos^{-1}(4\cos^3\theta-3\cos\theta)\quad[\text{ধরি,} x=\cos\theta]$\\$=\cos^{-1}\cos3\theta=3\theta=3\cos^{-1}x$\\$\therefore\frac{dy}{dx}=\frac{-3}{\sqrt{1-x^2}}\ (Ans.)$

**Final answer:** $-\frac{3}{\sqrt{1-x^2}}$

## ID 1224

**Question:** $\frac{d}{dx}\left(\frac{1}{2}\sin^{-1}\frac{10x}{1+25x^2}\right)$

**Solution:** $(xv)\ \frac{d}{dx}\left(\frac{1}{2}\sin^{-1}\frac{10x}{1+25x^2}\right)=\frac{d}{dx}\left(\frac{1}{2}\sin^{-1}\frac{2\cdot5x}{1+(5x)^2}\right)$\\$=\frac{d}{dx}\left(\frac{1}{2}\cdot2\tan^{-1}5x\right)=\frac{d}{dx}(\tan^{-1}5x)$\\$=\frac{1}{1+(5x)^2}\frac{d}{dx}(5x)=\frac{1}{1+25x^2}\ (Ans.)$

**Final answer:** $\frac{1}{1+25x^2}$

## ID 1225

**Question:** $\frac{d}{dx}\left[\sin^{-1}(\tan^{-1}x)\right]$

**Solution:** $(xvi)\ \frac{d}{dx}\left[\sin^{-1}(\tan^{-1}x)\right]$\\$=\frac{1}{\sqrt{1-(\tan^{-1}x)^2}}\frac{d}{dx}(\tan^{-1}x)$\\$=\frac{1}{\sqrt{1-(\tan^{-1}x)^2}}\cdot\frac{1}{1+x^2}$\\$=\frac{1}{(1+x^2)\sqrt{1-(\tan^{-1}x)^2}}\ (Ans.)$

**Final answer:** $\frac{1}{(1+x^2)\sqrt{1-(\tan^{-1}x)^2}}$

## ID 1226

**Question:** $\frac{d}{dx}(x\sin^{-1}x)$

**Solution:** $(xvii)\ \frac{d}{dx}(x\sin^{-1}x)$\\$=x\frac{d}{dx}(\sin^{-1}x)+\sin^{-1}x\frac{d}{dx}(x)$\\$=\frac{x}{\sqrt{1-x^2}}+\sin^{-1}x\ (Ans.)$

**Final answer:** $\frac{x}{\sqrt{1-x^2}}+\sin^{-1}x$

## ID 1227

**Question:** $\frac{d}{dx}\left[\cot^{-1}\left(\frac{1-x}{1+x}\right)\right]$

**Solution:** $(xviii)\ \cot^{-1}\frac{1-x}{1+x}=\tan^{-1}\frac{1+x}{1-x}$\\$=\tan^{-1}(1)+\tan^{-1}x=\frac{\pi}{4}+\tan^{-1}x$\\$\therefore\frac{d}{dx}\left(\cot^{-1}\frac{1-x}{1+x}\right)=\frac{d}{dx}\left(\frac{\pi}{4}+\tan^{-1}x\right)$\\$=0+\frac{1}{1+x^2}=\frac{1}{1+x^2}\ (Ans.)$

**Final answer:** $\frac{1}{1+x^2}$

## ID 1228

**Question:** $\frac{d}{dx}\left[\sin^{-1}\frac{4x}{1+4x^2}\right]$

**Solution:** $(xix)\ \sin^{-1}\frac{4x}{1+4x^2}=\sin^{-1}\frac{2\cdot2x}{1+(2x)^2}=2\tan^{-1}(2x)$\\$\therefore\frac{d}{dx}\left(\sin^{-1}\frac{4x}{1+4x^2}\right)=\frac{d}{dx}\{2\tan^{-1}(2x)\}$\\$=2\cdot\frac{1}{1+(2x)^2}\cdot\frac{d}{dx}(2x)=\frac{4}{1+4x^2}\ (Ans.)$

**Final answer:** $\frac{4}{1+4x^2}$

## ID 1229

**Question:** $\frac{d}{dx}\left[\sin^{-1}\frac{6x}{1+9x^2}\right]$

**Solution:** $(xx)\ \sin^{-1}\frac{6x}{1+9x^2}=\sin^{-1}\frac{2\cdot3x}{1+(3x)^2}=2\tan^{-1}(3x)$\\$\therefore\frac{d}{dx}\left(\sin^{-1}\frac{6x}{1+9x^2}\right)=\frac{d}{dx}\{2\tan^{-1}(3x)\}$\\$=2\cdot\frac{1}{1+(3x)^2}\cdot\frac{d}{dx}(3x)=\frac{6}{1+9x^2}\ (Ans.)$

**Final answer:** $\frac{6}{1+9x^2}$

## ID 1230

**Question:** $\frac{d}{dx}\left[\tan^{-1}\frac{4x}{\sqrt{1-4x^2}}\right]$

**Solution:** $(xxi)$ যদি, $y=\tan^{-1}\frac{4x}{\sqrt{1-4x^2}}\ \text{এবং}\ 2x=\sin\theta$\\$\therefore\frac{dx}{d\theta}=\frac{\cos\theta}{2}\ \text{এবং}\ \frac{d\theta}{dx}=\frac{2}{\cos\theta}$\\$y=\tan^{-1}\frac{2\sin\theta}{\sqrt{1-\sin^2\theta}}=\tan^{-1}\frac{2\sin\theta}{\cos\theta}=\tan^{-1}(2\tan\theta)$\\$\therefore\frac{dy}{dx}=\frac{1}{1+(2\tan\theta)^2}\cdot2\sec^2\theta\cdot\frac{2}{\cos\theta}$\\$=\frac{4}{(1+3\sin^2\theta)\sqrt{1-\sin^2\theta}}=\frac{4}{(1+12x^2)\sqrt{1-4x^2}}\ (Ans.)$

**Final answer:** $\frac{4}{(1+12x^2)\sqrt{1-4x^2}}$

## ID 1231

**Question:** $\frac{d}{dx}\left[\tan^{-1}\sqrt{\frac{1-\cos x}{1+\cos x}}\right]$

**Solution:** $(xxii)\ \tan^{-1}\sqrt{\frac{1-\cos x}{1+\cos x}}$\\$=\tan^{-1}\sqrt{\frac{2\sin^2\frac{x}{2}}{2\cos^2\frac{x}{2}}}=\tan^{-1}\sqrt{\tan^2\frac{x}{2}}$\\$=\tan^{-1}\tan\frac{x}{2}=\frac{x}{2}$\\$\therefore\frac{d}{dx}\left(\tan^{-1}\sqrt{\frac{1-\cos x}{1+\cos x}}\right)=\frac{d}{dx}\left(\frac{x}{2}\right)=\frac{1}{2}\ (Ans.)$

**Final answer:** $\frac{1}{2}$

## ID 1232

**Question:** $\frac{d}{dx}\left[\sin\left\{2\tan^{-1}\sqrt{\frac{1-x}{1+x}}\right\}\right]$

**Solution:** $10.(i)$ যদি, $y=\sin\left\{2\tan^{-1}\sqrt{\frac{1-x}{1+x}}\right\}$\\$=\sin\left\{2\tan^{-1}\sqrt{\frac{1-\cos2\theta}{1+\cos2\theta}}\right\}\quad[\text{মনে করি,} x=\cos2\theta]$\\$=\sin\left(2\tan^{-1}\sqrt{\frac{2\sin^2\theta}{2\cos^2\theta}}\right)=\sin(2\tan^{-1}\tan\theta)=\sin2\theta$\\$=\sqrt{1-x^2}$\\$\therefore\frac{dy}{dx}=\frac{-2x}{2\sqrt{1-x^2}}=-\frac{x}{\sqrt{1-x^2}}\ (Ans.)$

**Final answer:** $-\frac{x}{\sqrt{1-x^2}}$

## ID 1233

**Question:** $\frac{d}{dx}\left[\sin^{-1}\left(\frac{1-x^2}{1+x^2}\right)\right]$

**Solution:** $(ii)$ মনে করি, $y=\sin^{-1}\left(\frac{1-x^2}{1+x^2}\right)$।\\ধরি, $u=\frac{1-x^2}{1+x^2}$।\\$\therefore \frac{du}{dx}=\frac{(1+x^2)(-2x)-(1-x^2)(2x)}{(1+x^2)^2}=-\frac{4x}{(1+x^2)^2}$\\আবার, $1-u^2=1-\left(\frac{1-x^2}{1+x^2}\right)^2=\frac{4x^2}{(1+x^2)^2}$।\\সুতরাং $x>0$ হলে, $\sqrt{1-u^2}=\frac{2x}{1+x^2}$।\\$\therefore \frac{dy}{dx}=\frac{1}{\sqrt{1-u^2}}\frac{du}{dx}=-\frac{2}{1+x^2}\ (Ans.)$

**Final answer:** $-\frac{2}{1+x^2}$

## ID 1234

**Question:** $\frac{d}{dx}\left[\cos^4\left\{\cot^{-1}\sqrt{\frac{1-x}{1+x}}\right\}\right]$

**Solution:** $(iii)$ যদি, $y=\cos^4\left\{\cot^{-1}\sqrt{\frac{1-x}{1+x}}\right\}$\\$\text{ধরি,} x=\cos2\theta$\\$\therefore y=\cos^4\left\{\cot^{-1}\sqrt{\frac{1-\cos2\theta}{1+\cos2\theta}}\right\}=\cos^4\{\cot^{-1}(\tan\theta)\}$\\$=\cos^4\left\{\cot^{-1}\cot\left(\frac{\pi}{2}-\theta\right)\right\}=\cos^4\left(\frac{\pi}{2}-\theta\right)$\\$=\sin^4\theta=\frac{1}{4}(2\sin^2\theta)^2=\frac{1}{4}(1-\cos2\theta)^2=\frac{1}{4}(1-x)^2$\\$\therefore\frac{dy}{dx}=\frac{1}{4}\cdot2(1-x)(-1)=\frac{1}{2}(x-1)\ (Ans.)$

**Final answer:** $\frac{1}{2}(x-1)$

## ID 1235

**Question:** $\frac{d}{dx}\left(\tan^{-1}\frac{1+x}{1-x}\right)$

**Solution:** $11.(i)\ y=\tan^{-1}\frac{1+x}{1-x}$\\$=\tan^{-1}1+\tan^{-1}x=\tan^{-1}\tan\frac{\pi}{4}+\tan^{-1}x=\frac{\pi}{4}+\tan^{-1}x$\\$\therefore\frac{dy}{dx}=\frac{1}{1+x^2}\ (Ans.)$

**Final answer:** $\frac{1}{1+x^2}$

## ID 1236

**Question:** $\frac{d}{dx}\left[\tan^{-1}\left(\frac{a+bx}{b-ax}\right)\right]$

**Solution:** $(ii)$ মনে করি, $y=\tan^{-1}\left(\frac{a+bx}{b-ax}\right)=\tan^{-1}\left\{\frac{\frac{a}{b}+x}{1-\left(\frac{a}{b}\right)x}\right\}$\\$=\tan^{-1}\frac{a}{b}+\tan^{-1}x$\\$\therefore\frac{dy}{dx}=\frac{d}{dx}\left(\tan^{-1}\frac{a}{b}\right)+\frac{d}{dx}(\tan^{-1}x)$\\$=0+\frac{1}{1+x^2}=\frac{1}{1+x^2}\ (Ans.)$

**Final answer:** $\frac{1}{1+x^2}$

## ID 1237

**Question:** $\frac{d}{dx}\left[\tan^{-1}\left(\frac{a\cos x-b\sin x}{b\cos x+a\sin x}\right)\right]$

**Solution:** $(iii)\ \frac{d}{dx}\left[\tan^{-1}\left\{\frac{a\cos x-b\sin x}{b\cos x+a\sin x}\right\}\right]$\\$=\frac{d}{dx}\left[\tan^{-1}\left\{\frac{\frac{a}{b}-\tan x}{1+\frac{a}{b}\tan x}\right\}\right]$\\$=\frac{d}{dx}\left[\tan^{-1}\frac{a}{b}-\tan^{-1}\tan x\right]$\\$=0-1=-1\ (Ans.)$

**Final answer:** $-1$

## ID 1238

**Question:** $\frac{d}{dx}\left(\tan^{-1}\frac{4\sqrt{x}}{1-4x}+x^{\sin^{-1}x}\right)$

**Solution:** $(iv)$ ধরি, $t=\tan^{-1}\frac{4\sqrt{x}}{1-4x}+x^{\sin^{-1}x}=y+z$\\যেহেতু, $y=\tan^{-1}\frac{4\sqrt{x}}{1-4x}=\tan^{-1}\frac{2\cdot2\sqrt{x}}{1-(2\sqrt{x})^2}$\\$\therefore y=2\tan^{-1}(2\sqrt{x})$\\$\therefore\frac{dy}{dx}=2\frac{1}{1+4x}\frac{d}{dx}(2\sqrt{x})=\frac{2}{\sqrt{x}(1+4x)}$\\এবং $z=x^{\sin^{-1}x}$\\$\ln z=\sin^{-1}x\ln x$\\$\frac{1}{z}\frac{dz}{dx}=\sin^{-1}x\frac{d}{dx}(\ln x)+\ln x\frac{d}{dx}(\sin^{-1}x)$\\$\therefore\frac{dz}{dx}=x^{\sin^{-1}x}\left(\frac{\sin^{-1}x}{x}+\frac{\ln x}{\sqrt{1-x^2}}\right)$\\$\therefore\frac{dt}{dx}=\frac{2}{\sqrt{x}(1+4x)}+x^{\sin^{-1}x}\left(\frac{\sin^{-1}x}{x}+\frac{\ln x}{\sqrt{1-x^2}}\right)\ (Ans.)$

**Final answer:** $\frac{2}{\sqrt{x}(1+4x)}+x^{\sin^{-1}x}\left(\frac{\sin^{-1}x}{x}+\frac{\ln x}{\sqrt{1-x^2}}\right)$

## ID 1239

**Question:** $\frac{d}{dx}(\tan^{-1}e^x)$

**Solution:** $12.(i)\ \frac{d}{dx}\{\tan^{-1}(e^x)\}=\frac{1}{1+(e^x)^2}\frac{d}{dx}(e^x)=\frac{e^x}{1+e^{2x}}\ (Ans.)$

**Final answer:** $\frac{e^x}{1+e^{2x}}$

## ID 1240

**Question:** $\frac{d}{dx}\left[\tan^{-1}\left(\frac{\sqrt{1+x^2}-1}{x}\right)\right]$

**Solution:** $(ii)$ যদি, $y=\tan^{-1}\frac{\sqrt{1+x^2}-1}{x}$\\$\text{ধরি,} x=\tan\theta,\ \theta=\tan^{-1}x$\\$y=\tan^{-1}\frac{\sqrt{1+\tan^2\theta}-1}{\tan\theta}=\tan^{-1}\frac{\sec\theta-1}{\tan\theta}$\\$=\tan^{-1}\left(\frac{1-\cos\theta}{\sin\theta}\right)=\tan^{-1}\left(\frac{2\sin^2\frac{\theta}{2}}{2\sin\frac{\theta}{2}\cos\frac{\theta}{2}}\right)$\\$=\tan^{-1}\tan\frac{\theta}{2}=\frac{\theta}{2}=\frac{1}{2}\tan^{-1}x$\\$\therefore\frac{dy}{dx}=\frac{1}{2(1+x^2)}\ (Ans.)$

**Final answer:** $\frac{1}{2(1+x^2)}$

## ID 1241

**Question:** $\frac{d}{dx}\left[\tan^{-1}\left(\frac{3x-x^3}{1-3x^2}\right)\right]$

**Solution:** $(iii)\ \frac{d}{dx}\left[\tan^{-1}\left(\frac{3x-x^3}{1-3x^2}\right)\right]=\frac{d}{dx}(3\tan^{-1}x)$\\$=\frac{3}{1+x^2}\ (Ans.)$

**Final answer:** $\frac{3}{1+x^2}$

## ID 1242

**Question:** $\frac{d}{dx}\left[\cot^{-1}\left(\frac{x^2}{e^x}\right)+\cot^{-1}\left(\frac{e^x}{x^2}\right)\right]$

**Solution:** $(iv)\ y=\cot^{-1}\left(\frac{x^2}{e^x}\right)+\cot^{-1}\left(\frac{e^x}{x^2}\right)$\\$=\cot^{-1}\left(\frac{x^2}{e^x}\right)+\tan^{-1}\left(\frac{x^2}{e^x}\right)$\\$=\frac{\pi}{2}\quad[\text{কারণ}\ \tan^{-1}\theta+\cot^{-1}\theta=\frac{\pi}{2}]$\\$\therefore\frac{dy}{dx}=0\ (Ans.)$

**Final answer:** $0$

## ID 1243

**Question:** $\frac{d}{dx}\left[\ln\left(x-\sqrt{x^2-1}\right)\right]$

**Solution:** $1.(i)\ \frac{d}{dx}\left[\ln\left(x-\sqrt{x^2-1}\right)\right]$\\$=\frac{1}{x-\sqrt{x^2-1}}\cdot\frac{d}{dx}\left(x-\sqrt{x^2-1}\right)$\\$=\frac{1}{x-\sqrt{x^2-1}}\left\{1-\frac{x}{\sqrt{x^2-1}}\right\}$\\$=\frac{1}{x-\sqrt{x^2-1}}\left\{\frac{\sqrt{x^2-1}-x}{\sqrt{x^2-1}}\right\}=-\frac{1}{\sqrt{x^2-1}}\ (Ans.)$

**Final answer:** $-\frac{1}{\sqrt{x^2-1}}$

## ID 1244

**Question:** $\frac{d}{dx}\left[\ln\left\{\sqrt{x-2}+\sqrt{x+1}\right\}\right]$

**Solution:** $(ii)\ \frac{d}{dx}\left[\ln\{\sqrt{x-2}+\sqrt{x+1}\}\right]$\\$=\frac{1}{\sqrt{x-2}+\sqrt{x+1}}\cdot\frac{d}{dx}(\sqrt{x-2}+\sqrt{x+1})$\\$=\frac{1}{\sqrt{x-2}+\sqrt{x+1}}\left(\frac{1}{2\sqrt{x-2}}+\frac{1}{2\sqrt{x+1}}\right)$\\$=\frac{1}{2\sqrt{(x-2)(x+1)}}\ (Ans.)$

**Final answer:** $\frac{1}{2\sqrt{(x-2)(x+1)}}$

## ID 1245

**Question:** $\frac{d}{dx}\left[\ln\left(\frac{1+\sqrt{x}}{1-\sqrt{x}}\right)\right]$

**Solution:** $(iii)\ \frac{d}{dx}\left[\ln\left(\frac{1+\sqrt{x}}{1-\sqrt{x}}\right)\right]$\\$=\frac{d}{dx}\{\ln(1+\sqrt{x})-\ln(1-\sqrt{x})\}$\\$=\frac{1}{1+\sqrt{x}}\cdot\frac{1}{2\sqrt{x}}+\frac{1}{1-\sqrt{x}}\cdot\frac{1}{2\sqrt{x}}$\\$=\frac{2}{2\sqrt{x}(1-x)}=\frac{1}{\sqrt{x}(1-x)}\ (Ans.)$

**Final answer:** $\frac{1}{\sqrt{x}(1-x)}$

## ID 1246

**Question:** $\frac{d}{dx}\left[\ln\left(\frac{x^2+x+1}{x^2-x+1}\right)\right]$

**Solution:** $(iv)\ \frac{d}{dx}\left\{\ln\left(\frac{x^2+x+1}{x^2-x+1}\right)\right\}$\\$=\frac{d}{dx}\{\ln(x^2+x+1)-\ln(x^2-x+1)\}$\\$=\frac{2x+1}{x^2+x+1}-\frac{2x-1}{x^2-x+1}$\\$=\frac{2(1-x^2)}{x^4+x^2+1}\ (Ans.)$

**Final answer:** $\frac{2(1-x^2)}{x^4+x^2+1}$

## ID 1247

**Question:** $\frac{d}{dx}\left[\ln\left\{\frac{\sqrt{x+1}-1}{\sqrt{x+1}+1}\right\}\right]$

**Solution:** $(v)\ \frac{d}{dx}\left[\ln\left\{\frac{\sqrt{x+1}-1}{\sqrt{x+1}+1}\right\}\right]$\\$=\frac{d}{dx}\{\ln(\sqrt{x+1}-1)-\ln(\sqrt{x+1}+1)\}$\\$=\frac{1}{\sqrt{x+1}-1}\frac{1}{2\sqrt{x+1}}-\frac{1}{\sqrt{x+1}+1}\frac{1}{2\sqrt{x+1}}$\\$=\frac{1}{x\sqrt{x+1}}\ (Ans.)$

**Final answer:** $\frac{1}{x\sqrt{x+1}}$

## ID 1248

**Question:** $\frac{d}{dx}\left[\ln\sqrt{\frac{1-\cos x}{1+\cos x}}\right]$

**Solution:** $(vi)$ যদি, $y=\ln\sqrt{\frac{1-\cos x}{1+\cos x}}$\\$=\ln\sqrt{\frac{2\sin^2\frac{x}{2}}{2\cos^2\frac{x}{2}}}=\ln\sqrt{\tan^2\frac{x}{2}}=\ln\tan\frac{x}{2}$\\$\therefore\frac{dy}{dx}=\frac{1}{\tan\frac{x}{2}}\sec^2\frac{x}{2}\cdot\frac{1}{2}=\frac{1}{\sin x}=\cosec x\ (Ans.)$

**Final answer:** $\cosec x$

## ID 1249

**Question:** $\frac{d}{dx}\left[\ln\sqrt[3]{\frac{1-\cos x}{1+\cos x}}\right]$

**Solution:** $(vii)\ \ln\sqrt[3]{\frac{1-\cos x}{1+\cos x}}=\ln\left(\frac{2\sin^2\frac{x}{2}}{2\cos^2\frac{x}{2}}\right)^{\frac{1}{3}}$\\$=\frac{1}{3}\ln\tan^2\frac{x}{2}=\frac{2}{3}\ln\tan\frac{x}{2}$\\$\therefore\frac{d}{dx}\left(\ln\sqrt[3]{\frac{1-\cos x}{1+\cos x}}\right)=\frac{2}{3}\frac{\sec^2\frac{x}{2}}{\tan\frac{x}{2}}\cdot\frac{1}{2}$\\$=\frac{2}{3\sin x}=\frac{2}{3}\cosec x\ (Ans.)$

**Final answer:** $\frac{2}{3}\cosec x$

## ID 1250

**Question:** $\frac{d}{dx}\left[\ln\left(\sqrt{x-a}+\sqrt{x-b}\right)\right]$

**Solution:** $(viii)\ \frac{d}{dx}\left[\ln(\sqrt{x-a}+\sqrt{x-b})\right]$\\$=\frac{1}{\sqrt{x-a}+\sqrt{x-b}}\cdot\frac{d}{dx}(\sqrt{x-a}+\sqrt{x-b})$\\$=\frac{1}{\sqrt{x-a}+\sqrt{x-b}}\left(\frac{1}{2\sqrt{x-a}}+\frac{1}{2\sqrt{x-b}}\right)$\\$=\frac{1}{2\sqrt{(x-a)(x-b)}}\ (Ans.)$

**Final answer:** $\frac{1}{2\sqrt{(x-a)(x-b)}}$

## ID 1251

**Question:** $\frac{d}{dx}\left(\frac{x}{1+\sqrt{1-x^2}}\right)^n$

**Solution:** $2.(i)\ \frac{d}{dx}\left[\frac{x}{1+\sqrt{1-x^2}}\right]^n$\\$=n\left(\frac{x}{1+\sqrt{1-x^2}}\right)^{n-1}\frac{d}{dx}\left(\frac{x}{1+\sqrt{1-x^2}}\right)$\\$=\frac{n}{\sqrt{1-x^2}}\left(\frac{x}{1+\sqrt{1-x^2}}\right)^n\ (Ans.)$

**Final answer:** $\frac{n}{\sqrt{1-x^2}}\left(\frac{x}{1+\sqrt{1-x^2}}\right)^n$

## ID 1252

**Question:** $\frac{d}{dx}\left(\frac{1-x^2}{1+x^2}\right)^2$

**Solution:** $(ii)$ যদি, $y=\left(\frac{1-x^2}{1+x^2}\right)^2,\ x=\tan\theta$\\$\therefore y=\left(\frac{1-\tan^2\theta}{1+\tan^2\theta}\right)^2=\cos^2 2\theta$\\$\frac{dy}{d\theta}=-4\cos2\theta\sin2\theta,\quad \frac{dx}{d\theta}=\sec^2\theta$\\$\therefore\frac{dy}{dx}=\frac{-4\cos2\theta\sin2\theta}{\sec^2\theta}=\frac{-8x(1-x^2)}{(1+x^2)^3}\ (Ans.)$

**Final answer:** $\frac{-8x(1-x^2)}{(1+x^2)^3}$

## ID 1253

**Question:** $\frac{d}{dx}\sqrt{\frac{1-x}{1+x}}$

**Solution:** $(iii)\ \frac{d}{dx}\left(\sqrt{\frac{1-x}{1+x}}\right)=\frac{d}{dx}\left\{\frac{(1-x)^{\frac{1}{2}}}{(1+x)^{\frac{1}{2}}}\right\}$\\$=\frac{(1+x)^{\frac{1}{2}}\frac{d}{dx}(1-x)^{\frac{1}{2}}-(1-x)^{\frac{1}{2}}\frac{d}{dx}(1+x)^{\frac{1}{2}}}{1+x}$\\$=-\frac{1}{(1+x)\sqrt{1-x^2}}\ (Ans.)$

**Final answer:** $-\frac{1}{(1+x)\sqrt{1-x^2}}$

## ID 1254

**Question:** $\frac{d}{dx}(1+\sin2x)^2$

**Solution:** $(iv)$ যদি, $y=(1+\sin2x)^2$\\$\therefore\frac{dy}{dx}=2(1+\sin2x)\frac{d}{dx}(1+\sin2x)$\\$=2(1+\sin2x)\cos2x\cdot2=4\cos2x(1+\sin2x)\ (Ans.)$

**Final answer:** $4\cos2x(1+\sin2x)$

## ID 1255

**Question:** $\frac{d}{dx}\left(\frac{(x+1)^2\sqrt{x-1}}{(x+4)^3e^x}\right)$

**Solution:** $(v)$ যদি, $y=\frac{(x+1)^2\sqrt{x-1}}{(x+4)^3e^x}$\\$\therefore \ln y=2\ln(x+1)+\frac{1}{2}\ln(x-1)-3\ln(x+4)-x$\\$\therefore\frac{1}{y}\frac{dy}{dx}=\frac{2}{x+1}+\frac{1}{2(x-1)}-\frac{3}{x+4}-1$\\$\therefore\frac{dy}{dx}=\frac{(x+1)^2\sqrt{x-1}}{(x+4)^3e^x}\left[\frac{2}{x+1}+\frac{1}{2(x-1)}-\frac{3}{x+4}-1\right]\ (Ans.)$

**Final answer:** $\frac{(x+1)^2\sqrt{x-1}}{(x+4)^3e^x}\left[\frac{2}{x+1}+\frac{1}{2(x-1)}-\frac{3}{x+4}-1\right]$

## ID 1256

**Question:** $\frac{d}{dx}\left(x^3\sqrt{\frac{x^2+4}{x^2+3}}\right)$

**Solution:** $(vi)$ যদি, $y=x^3\sqrt{\frac{x^2+4}{x^2+3}}$\\$\ln y=3\ln x+\frac{1}{2}\ln(x^2+4)-\frac{1}{2}\ln(x^2+3)$\\$\frac{1}{y}\frac{dy}{dx}=\frac{3}{x}+\frac{x}{x^2+4}-\frac{x}{x^2+3}$\\$\therefore\frac{dy}{dx}=x^3\sqrt{\frac{x^2+4}{x^2+3}}\left[\frac{3}{x}+\frac{x}{x^2+4}-\frac{x}{x^2+3}\right]\ (Ans.)$

**Final answer:** $x^3\sqrt{\frac{x^2+4}{x^2+3}}\left[\frac{3}{x}+\frac{x}{x^2+4}-\frac{x}{x^2+3}\right]$

## ID 1257

**Question:** $\frac{d}{dx}\sqrt{\frac{(x-1)(x-2)}{(x-3)(x-4)}}$

**Solution:** $(vii)$ যদি, $y=\sqrt{\frac{(x-1)(x-2)}{(x-3)(x-4)}}$\\$\ln y=\frac{1}{2}\ln(x-1)+\frac{1}{2}\ln(x-2)-\frac{1}{2}\ln(x-3)-\frac{1}{2}\ln(x-4)$\\$\frac{1}{y}\frac{dy}{dx}=\frac{1}{2}\left(\frac{1}{x-1}+\frac{1}{x-2}-\frac{1}{x-3}-\frac{1}{x-4}\right)$\\$\therefore\frac{dy}{dx}=\frac{1}{2}\sqrt{\frac{(x-1)(x-2)}{(x-3)(x-4)}}\left(\frac{1}{x-1}+\frac{1}{x-2}-\frac{1}{x-3}-\frac{1}{x-4}\right)\ (Ans.)$

**Final answer:** $\frac{1}{2}\sqrt{\frac{(x-1)(x-2)}{(x-3)(x-4)}}\left(\frac{1}{x-1}+\frac{1}{x-2}-\frac{1}{x-3}-\frac{1}{x-4}\right)$

## ID 1258

**Question:** $\frac{d}{dx}\left(\frac{e^{x^2}\tan^{-1}x}{\sqrt{1+x^2}}\right)$

**Solution:** $(viii)$ যদি, $y=\frac{e^{x^2}\tan^{-1}x}{\sqrt{1+x^2}}$\\$\ln y=x^2+\ln\tan^{-1}x-\frac{1}{2}\ln(1+x^2)$\\$\frac{1}{y}\frac{dy}{dx}=2x+\frac{1}{(1+x^2)\tan^{-1}x}-\frac{x}{1+x^2}$\\$\therefore\frac{dy}{dx}=\frac{e^{x^2}\tan^{-1}x}{\sqrt{1+x^2}}\left[2x+\frac{1}{(1+x^2)\tan^{-1}x}-\frac{x}{1+x^2}\right]\ (Ans.)$

**Final answer:** $\frac{e^{x^2}\tan^{-1}x}{\sqrt{1+x^2}}\left[2x+\frac{1}{(1+x^2)\tan^{-1}x}-\frac{x}{1+x^2}\right]$

## ID 1259

**Question:** $\frac{d}{dx}\left(\frac{x\cos^{-1}x}{\sqrt{1-x^2}}\right)$

**Solution:** $(ix)\ y=\frac{x\cos^{-1}x}{\sqrt{1-x^2}}$\\$\ln y=\ln x+\ln\cos^{-1}x-\ln\sqrt{1-x^2}$\\$\frac{1}{y}\frac{dy}{dx}=\frac{1}{x}-\frac{1}{\cos^{-1}x\sqrt{1-x^2}}+\frac{x}{1-x^2}$\\$\therefore\frac{dy}{dx}=\frac{x\cos^{-1}x}{\sqrt{1-x^2}}\left[\frac{1}{x}-\frac{1}{\cos^{-1}x\sqrt{1-x^2}}+\frac{x}{1-x^2}\right]\ (Ans.)$

**Final answer:** $\frac{x\cos^{-1}x}{\sqrt{1-x^2}}\left[\frac{1}{x}-\frac{1}{\cos^{-1}x\sqrt{1-x^2}}+\frac{x}{1-x^2}\right]$

## ID 1260

**Question:** $\frac{d}{dx}\left(x^2\sqrt{\frac{1+x}{1-x}}\right)$

**Solution:** $(x)$ যদি, $y=x^2\sqrt{\frac{1+x}{1-x}}$\\$\ln y=2\ln x+\frac{1}{2}\{\ln(1+x)-\ln(1-x)\}$\\$\frac{1}{y}\frac{dy}{dx}=\frac{2}{x}+\frac{1}{2}\left(\frac{1}{1+x}+\frac{1}{1-x}\right)$\\$\therefore\frac{dy}{dx}=x^2\sqrt{\frac{1+x}{1-x}}\left[\frac{2}{x}+\frac{1}{(1+x)(1-x)}\right]$\\$=2x\sqrt{\frac{1+x}{1-x}}+\frac{x^2}{\sqrt{1+x}(1-x)^{\frac{3}{2}}}\ (Ans.)$

**Final answer:** $2x\sqrt{\frac{1+x}{1-x}}+\frac{x^2}{\sqrt{1+x}(1-x)^{\frac{3}{2}}}$

## ID 1261

**Question:** $\frac{d}{dx}(x^x)$

**Solution:** $3.(i)$ মনে করি, $y=x^x$\\$\ln y=x\ln x$ [উভয় পাশে ln নিয়ে]\\$\frac{1}{y}\frac{dy}{dx}=\ln x+x\cdot\frac{1}{x}=\ln x+1$\\$\therefore\frac{dy}{dx}=x^x[\ln x+1]\ (Ans.)$

**Final answer:** $x^x[\ln x+1]$

## ID 1262

**Question:** $\frac{d}{dx}(x^{\frac{1}{x}})$

**Solution:** $(ii)$ যদি, $y=x^{\frac{1}{x}}$\\$\ln y=\frac{1}{x}\ln x$ [উভয় পাশে ln নিয়ে]\\$\frac{1}{y}\frac{dy}{dx}=\frac{1}{x}\frac{1}{x}+\ln(x)(-1)\frac{1}{x^2}$\\$\frac{dy}{dx}=x^{\frac{1}{x}}\frac{1}{x^2}(1-\ln x)=x^{\frac{1}{x}-2}[1-\ln x]\ (Ans.)$

**Final answer:** $x^{\frac{1}{x}-2}[1-\ln x]$

## ID 1263

**Question:** $\frac{d}{dx}\left((\sqrt{x})^{\sqrt{x}}\right)$

**Solution:** $(iii)$ মনে করি, $y=(\sqrt{x})^{\sqrt{x}}$\\$\ln y=\sqrt{x}\ln x^{\frac{1}{2}}=\frac{1}{2}\sqrt{x}\ln x$\\$\frac{1}{y}\frac{dy}{dx}=\frac{1}{2}\left(\sqrt{x}\cdot\frac{1}{x}+\frac{1}{2\sqrt{x}}\ln x\right)$\\$\frac{dy}{dx}=\frac{1}{2}(\sqrt{x})^{\sqrt{x}}\left[\frac{1}{\sqrt{x}}+\frac{1}{2\sqrt{x}}\ln x\right]$\\$=\frac{1}{4}(\sqrt{x})^{\sqrt{x}-1}[2+\ln x]\ (Ans.)$

**Final answer:** $\frac{1}{4}(\sqrt{x})^{\sqrt{x}-1}[2+\ln x]$

## ID 1264

**Question:** $\frac{d}{dx}\left((1+x^2)^{2x}\right)$

**Solution:** $(iv)$ মনে করি, $y=(1+x^2)^{2x}$\\$\ln y=2x\ln(1+x^2)$\\$\frac{1}{y}\frac{dy}{dx}=2x\cdot\frac{1}{1+x^2}\cdot2x+2\ln(1+x^2)$\\$\therefore\frac{dy}{dx}=(1+x^2)^{2x}\left[\frac{4x^2}{1+x^2}+2\ln(1+x^2)\right]\ (Ans.)$

**Final answer:** $(1+x^2)^{2x}\left[\frac{4x^2}{1+x^2}+2\ln(1+x^2)\right]$

## ID 1265

**Question:** $\frac{d}{dx}\left((1+x^2)^{x^2}\right)$

**Solution:** $(v)$ মনে করি, $y=(1+x^2)^{x^2}$\\$\ln y=x^2\ln(1+x^2)$\\$\frac{1}{y}\frac{dy}{dx}=x^2\frac{2x}{1+x^2}+2x\ln(1+x^2)$\\$\therefore\frac{dy}{dx}=2x(1+x^2)^{x^2}\left[\frac{x^2}{1+x^2}+\ln(1+x^2)\right]\ (Ans.)$

**Final answer:** $2x(1+x^2)^{x^2}\left[\frac{x^2}{1+x^2}+\ln(1+x^2)\right]$

## ID 1266

**Question:** $\frac{d}{dx}\left((1+x)^x\right)$

**Solution:** $(vi)$ যদি, $y=(1+x)^x$\\$\ln y=x\ln(1+x)$\\$\frac{1}{y}\frac{dy}{dx}=\ln(1+x)+\frac{x}{1+x}$\\$\frac{dy}{dx}=y\left\{\ln(1+x)+\frac{x}{1+x}\right\}$\\$=\frac{(1+x)^x}{1+x}\{(1+x)\ln(1+x)+x\}$\\$=(1+x)^{x-1}\{(1+x)\ln(1+x)+x\}\ (Ans.)$

**Final answer:** $(1+x)^{x-1}\{(1+x)\ln(1+x)+x\}$

## ID 1267

**Question:** $\frac{d}{dx}\left((\sin x)^x\right)$

**Solution:** $(vii)$ যদি, $y=(\sin x)^x$\\$\ln y=x\ln\sin x$\\$\frac{1}{y}\frac{dy}{dx}=x\cdot\frac{1}{\sin x}\cos x+\ln\sin x$\\$\therefore\frac{dy}{dx}=(\sin x)^x(x\cot x+\ln\sin x)\ (Ans.)$

**Final answer:** $(\sin x)^x(x\cot x+\ln\sin x)$

## ID 1268

**Question:** $\frac{d}{dx}\left(x^{\cos x}\right)$

**Solution:** $(viii)$ যদি, $y=x^{\cos x}$\\$\ln y=\cos x\ln x$\\$\frac{1}{y}\frac{dy}{dx}=\ln x(-\sin x)+\cos x\cdot\frac{1}{x}$\\$\therefore\frac{dy}{dx}=x^{\cos x}\left[-\sin x\ln x+\frac{\cos x}{x}\right]\ (Ans.)$

**Final answer:** $x^{\cos x}\left[-\sin x\ln x+\frac{\cos x}{x}\right]$

## ID 1269

**Question:** $\frac{d}{dx}\left(x^{\tan^{-1}x}\right)$

**Solution:** $(ix)$ যদি, $y=x^{\tan^{-1}x}$\\$\ln y=(\tan^{-1}x)\ln x$\\$\frac{1}{y}\frac{dy}{dx}=\tan^{-1}x\cdot\frac{1}{x}+\ln x\cdot\frac{1}{1+x^2}$\\$\therefore\frac{d}{dx}(x^{\tan^{-1}x})=x^{\tan^{-1}x}\left(\frac{\tan^{-1}x}{x}+\frac{\ln x}{1+x^2}\right)\ (Ans.)$

**Final answer:** $x^{\tan^{-1}x}\left(\frac{\tan^{-1}x}{x}+\frac{\ln x}{1+x^2}\right)$

## ID 1270

**Question:** $\frac{d}{dx}\left((\cot x)^{\tan x}\right)$

**Solution:** $(x)$ মনে করি, $y=(\cot x)^{\tan x}$\\$\ln y=\tan x\ln(\cot x)$\\$\frac{1}{y}\frac{dy}{dx}=\tan x\cdot\frac{1}{\cot x}(-\cosec^2x)+\ln(\cot x)\sec^2x$\\$=\sec^2x\{\ln(\cot x)-1\}$\\$\therefore\frac{dy}{dx}=(\cot x)^{\tan x}\left[\sec^2x\{\ln(\cot x)-1\}\right]\ (Ans.)$

**Final answer:** $(\cot x)^{\tan x}\left[\sec^2x\{\ln(\cot x)-1\}\right]$

## ID 1271

**Question:** $\frac{d}{dx}\left((\sin x)^{\tan x}\right)$

**Solution:** $(xi)$ যদি, $y=(\sin x)^{\tan x}$\\$\ln y=\tan x\ln(\sin x)$\\$\frac{1}{y}\frac{dy}{dx}=\tan x\cdot\frac{1}{\sin x}\cos x+\sec^2x\ln(\sin x)$\\$=1+\sec^2x\ln(\sin x)$\\$\therefore\frac{dy}{dx}=(\sin x)^{\tan x}\{1+\sec^2x\ln(\sin x)\}\ (Ans.)$

**Final answer:** $(\sin x)^{\tan x}\{1+\sec^2x\ln(\sin x)\}$

## ID 1272

**Question:** $\frac{d}{dx}\left(x^{\ln x}\right)$

**Solution:** $(xii)$ মনে করি, $y=x^{\ln x}$\\$\ln y=\ln x\cdot\ln x=(\ln x)^2$\\$\frac{1}{y}\frac{dy}{dx}=2\ln x\cdot\frac{1}{x}$\\$\therefore\frac{dy}{dx}=\frac{2y}{x}\ln x=\frac{2}{x}x^{\ln x}\ln x$\\$\therefore\frac{dy}{dx}=2x^{\ln x-1}\ln x\ (Ans.)$

**Final answer:** $2x^{\ln x-1}\ln x$

## ID 1273

**Question:** $\frac{d}{dx}\left\{x^x+(\sin x)^{\ln x}\right\}$

**Solution:** $4.(i)\ y=y_1+y_2$\\$\text{ধরি,} y_1=x^x,\quad y_2=(\sin x)^{\ln x}$\\$\text{এখন,} y_1=x^x\quad\therefore \ln y_1=x\ln x$\\$\therefore\frac{1}{y_1}\frac{dy_1}{dx}=1+\ln x$\\$\therefore\frac{dy_1}{dx}=x^x(1+\ln x)$\\$\text{ধরি,} y_2=(\sin x)^{\ln x}$\\$\ln y_2=\ln x\ln\sin x$\\$\therefore\frac{1}{y_2}\frac{dy_2}{dx}=\ln x\cot x+\frac{\ln\sin x}{x}$\\$\therefore\frac{dy_2}{dx}=(\sin x)^{\ln x}\left(\cot x\ln x+\frac{\ln\sin x}{x}\right)$\\$\therefore\frac{dy}{dx}=x^x(1+\ln x)+(\sin x)^{\ln x}\left(\cot x\ln x+\frac{\ln\sin x}{x}\right)\ (Ans.)$

**Final answer:** $x^x(1+\ln x)+(\sin x)^{\ln x}\left(\cot x\ln x+\frac{\ln\sin x}{x}\right)$

## ID 1274

**Question:** $\frac{d}{dx}\left\{x^{\sin x}+(\sin x)^x\right\}$

**Solution:** $(ii)$ মনে করি, $y=x^{\sin x}+(\sin x)^x$\\$=e^{\sin x\ln x}+e^{x\ln(\sin x)}$\\$\therefore\frac{dy}{dx}=e^{\sin x\ln x}\left(\sin x\cdot\frac{1}{x}+\cos x\ln x\right)+e^{x\ln\sin x}\{\ln(\sin x)+x\cot x\}$\\$=x^{\sin x}\left(x^{-1}\sin x+\ln x\cos x\right)+(\sin x)^x\{\ln(\sin x)+x\cot x\}\ (Ans.)$

**Final answer:** $x^{\sin x}\left(x^{-1}\sin x+\ln x\cos x\right)+(\sin x)^x\{\ln(\sin x)+x\cot x\}$

## ID 1275

**Question:** $\frac{d}{dx}\left(e^{x^2}+x^{x^2}\right)$

**Solution:** $(iii)$ যদি, $y=e^{x^2}+x^{x^2}$\\$=u+v\quad[\text{ধরি,} u=e^{x^2}\ \text{ও}\ v=x^{x^2}]$\\$\therefore\frac{dy}{dx}=\frac{du}{dx}+\frac{dv}{dx}$\\$u=e^{x^2}\quad\therefore\frac{du}{dx}=2xe^{x^2}$\\$\text{আবার,} v=x^{x^2}\quad\therefore\ln v=x^2\ln x$\\$\frac{1}{v}\frac{dv}{dx}=x+2x\ln x$\\$\therefore\frac{dv}{dx}=x^{x^2+1}(1+2\ln x)$\\$\therefore\frac{dy}{dx}=2xe^{x^2}+x^{x^2+1}(1+2\ln x)\ (Ans.)$

**Final answer:** $2xe^{x^2}+x^{x^2+1}(1+2\ln x)$

## ID 1276

**Question:** $\frac{d}{dx}\left((x^x)^x\right)$

**Solution:** $5.(i)$ মনে করি, $y=(x^x)^x=x^{x^2}$\\$\text{তাহলে,} \ln y=x^2\ln x$ [উভয় পাশে ln নিয়ে]\\$\frac{1}{y}\frac{dy}{dx}=x^2\cdot\frac{1}{x}+2x\ln x=x(1+2\ln x)$\\$\therefore\frac{dy}{dx}=x^{x^2}x(1+2\ln x)\ (Ans.)$

**Final answer:** $x^{x^2}x(1+2\ln x)$

## ID 1277

**Question:** $\frac{d}{dx}\left(x^x\ln x\right)$

**Solution:** $(ii)$ মনে করি, $y=x^x\ln x$\\$\ln y=\ln(x^x\ln x)=x\ln x+\ln(\ln x)$\\$\frac{1}{y}\frac{dy}{dx}=1+\ln x+\frac{1}{x\ln x}$\\$=\frac{1+x\ln x(1+\ln x)}{x\ln x}$\\$\therefore\frac{dy}{dx}=x^x\ln x\cdot\frac{1+x\ln x(1+\ln x)}{x\ln x}$\\$=x^{x-1}\{1+x\ln x(1+\ln x)\}\ (Ans.)$

**Final answer:** $x^{x-1}\{1+x\ln x(1+\ln x)\}$

## ID 1278

**Question:** $\frac{d}{dx}\left(x^x\log_{10}x\right)$

**Solution:** $(iii)$ মনে করি, $y=x^x\log_{10}x$\\$\ln y=\ln(x^x\log_{10}x)=x\ln x+\ln(\log_{10}x)$\\$\frac{1}{y}\frac{dy}{dx}=1+\ln x+\frac{1}{\log_{10}x}\cdot\frac{1}{x\ln10}$\\$\therefore\frac{dy}{dx}=x^x\log_{10}x\left(1+\ln x+\frac{1}{x\log_{10}x\ln10}\right)$\\$=x^x\log_{10}x(1+\ln x)+\frac{x^x}{x\ln10}\ (Ans.)$

**Final answer:** $x^x\log_{10}x(1+\ln x)+\frac{x^x}{x\ln10}$

## ID 1279

**Question:** $\frac{d}{dx}\left(e^{e^x}\right)$

**Solution:** $6.(i)$ যদি, $y=e^{e^x}$\\$\ln y=e^x\quad\therefore\frac{1}{y}\frac{dy}{dx}=e^x$\\$\therefore\frac{dy}{dx}=ye^x=e^{e^x}e^x\ (Ans.)$

**Final answer:** $e^{e^x}e^x$

## ID 1280

**Question:** $\frac{d}{dx}\left(x^{e^x}\right)$

**Solution:** $(ii)$ যদি, $y=x^{e^x}$\\$\ln y=e^x\ln x$\\$\frac{1}{y}\frac{dy}{dx}=e^x\frac{d}{dx}(\ln x)+\ln x\frac{d}{dx}(e^x)$\\$\therefore\frac{dy}{dx}=e^x x^{e^x}\left(\frac{1}{x}+\ln x\right)\ (Ans.)$

**Final answer:** $e^x x^{e^x}\left(\frac{1}{x}+\ln x\right)$

## ID 1281

**Question:** $\frac{d}{dx}\left(e^{x^x}\right)$

**Solution:** $(iii)$ মনে করি, $y=e^{x^x}$\\$\ln y=x^x$\\$\ln(\ln y)=x\ln x$ [উভয় পাশে ln নিয়ে]\\$\frac{1}{\ln y}\cdot\frac{1}{y}\frac{dy}{dx}=1+\ln x$\\$\therefore\frac{dy}{dx}=e^{x^x}x^x(1+\ln x)\ (Ans.)$

**Final answer:** $e^{x^x}x^x(1+\ln x)$

## ID 1282

**Question:** $\frac{d}{dx}\left(a^{\ln(\cos x)}\right)$

**Solution:** $(iv)$ মনে করি, $y=a^{\ln(\cos x)}$\\$\frac{dy}{dx}=a^{\ln(\cos x)}\ln a\cdot\frac{d}{dx}\{\ln(\cos x)\}$\\$=a^{\ln(\cos x)}\ln a\cdot\frac{-\sin x}{\cos x}$\\$=-a^{\ln(\cos x)}\ln a\tan x\ (Ans.)$

**Final answer:** $-a^{\ln(\cos x)}\ln a\tan x$

## ID 1283

**Question:** $\frac{d}{dx}\left(a^{a^x}\right)$

**Solution:** $(v)$ মনে করি, $y=a^{a^x}$\\$\ln y=a^x\ln a$ [উভয় পাশে ln নিয়ে]\\$\frac{1}{y}\frac{dy}{dx}=\ln a\cdot a^x\ln a$\\$\therefore\frac{dy}{dx}=a^{a^x}a^x(\ln a)^2\ (Ans.)$

**Final answer:** $a^{a^x}a^x(\ln a)^2$

## ID 1284

**Question:** $\frac{dy}{dx},\ y=x^{x+x^{x+\cdots\infty}}$

**Solution:** $(vi)$ দেওয়া আছে, $y=x^{x+x^{x+\cdots\infty}}$\\$\text{বা,} y=x^y$\\$\ln y=y\ln x$ [উভয় পাশে ln নিয়ে]\\$x-\text{এর সাপেক্ষে উভয় পক্ষকে অন্তরীকরণ করে,}$\\$\frac{1}{y}\frac{dy}{dx}=\frac{y}{x}+\ln x\frac{dy}{dx}$\\$\frac{dy}{dx}\left(\frac{1}{y}-\ln x\right)=\frac{y}{x}$\\$\therefore\frac{dy}{dx}=\frac{y^2}{x(1-y\ln x)}\ (Ans.)$

**Final answer:** $\frac{y^2}{x(1-y\ln x)}$

## ID 1285

**Question:** $\frac{d}{dx}\left(a^{\cos x}\right)$

**Solution:** $(vii)\ \frac{d}{dx}(a^{\cos x})=a^{\cos x}\ln a\cdot\frac{d}{dx}(\cos x)$\\$=a^{\cos x}\ln a(-\sin x)=-a^{\cos x}\sin x\ln a\ (Ans.)$

**Final answer:** $-a^{\cos x}\sin x\ln a$

## ID 1286

**Question:** $\frac{d}{dx}\left(a^{px+q}\right)$

**Solution:** $(viii)$ যদি, $y=a^{px+q}$\\$\therefore\frac{dy}{dx}=a^{px+q}\ln a\frac{d}{dx}(px+q)$\\$=a^{px+q}\ln a(p+0)=p\ln a\,a^{px+q}\ (Ans.)$

**Final answer:** $p\ln a\,a^{px+q}$

## ID 1287

**Question:** $\frac{d}{dx}(\log_{\cos x}\tan x)$

**Solution:** $7.(i)\ \frac{d}{dx}(\log_{\cos x}\tan x)=\frac{d}{dx}\left(\frac{\ln\tan x}{\ln\cos x}\right)$\\$=\frac{\ln(\cos x)\frac{d}{dx}(\ln\tan x)-\ln(\tan x)\frac{d}{dx}(\ln\cos x)}{\{\ln(\cos x)\}^2}$\\$=\frac{\ln(\cos x)\frac{1}{\tan x}\sec^2x-\ln(\tan x)\frac{1}{\cos x}(-\sin x)}{\{\ln(\cos x)\}^2}$\\$=\frac{\sec x\cosec x\ln(\cos x)+\tan x\ln(\tan x)}{\{\ln(\cos x)\}^2}\ (Ans.)$

**Final answer:** $\frac{\sec x\cosec x\ln(\cos x)+\tan x\ln(\tan x)}{\{\ln(\cos x)\}^2}$

## ID 1288

**Question:** $\frac{d}{dx}(\log_ax+\log_xa)$

**Solution:** $(ii)$ যদি, $y=\log_ax+\log_xa=y_1+y_2$\\$\text{তাহলে,} y_1=\log_ax=\frac{\ln x}{\ln a}$\\$\therefore\frac{dy_1}{dx}=\frac{1}{x\ln a}$\\$\text{আবার,} y_2=\log_xa=\frac{\ln a}{\ln x}$\\$\therefore\frac{dy_2}{dx}=-\frac{\ln a}{x(\ln x)^2}$\\$\therefore\frac{dy}{dx}=\frac{1}{x\ln a}-\frac{\ln a}{x(\ln x)^2}$\\$=\frac{(\ln x)^2-(\ln a)^2}{x\ln a(\ln x)^2}\ (Ans.)$

**Final answer:** $\frac{(\ln x)^2-(\ln a)^2}{x\ln a(\ln x)^2}$

## ID 1289

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $x^4+x^2y^2+y^4=0$

**Solution:** $1.(i)$ দেওয়া আছে, $x^4+x^2y^2+y^4=0$\\$x-\text{এর সাপেক্ষে অন্তরীকরণ করে পাই,}$\\$\therefore 4x^3+2xy^2+2x^2y\frac{dy}{dx}+4y^3\frac{dy}{dx}=0$\\$\therefore 2y(x^2+2y^2)\frac{dy}{dx}=-(4x^3+2xy^2)=-2x(2x^2+y^2)$\\$\therefore\frac{dy}{dx}=-\frac{x(2x^2+y^2)}{y(x^2+2y^2)}\ (Ans.)$

**Final answer:** $-\frac{x(2x^2+y^2)}{y(x^2+2y^2)}$

## ID 1290

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $x^3y+xy^3=2$

**Solution:** $(ii)$ দেওয়া আছে, $x^3y+xy^3=2$\\$x-\text{এর সাপেক্ষে অন্তরীকরণ করে পাই,}$\\$\therefore 3x^2y+x^3\frac{dy}{dx}+y^3+3xy^2\frac{dy}{dx}=0$\\$\therefore (x^3+3xy^2)\frac{dy}{dx}=-(3x^2y+y^3)$\\$\therefore\frac{dy}{dx}=-\frac{(3x^2y+y^3)}{x^3+3xy^2}=-\frac{y(3x^2+y^2)}{x(x^2+3y^2)}\ (Ans.)$

**Final answer:** $-\frac{y(3x^2+y^2)}{x(x^2+3y^2)}$

## ID 1291

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $y=\tan(x+y)$

**Solution:** $2.(i)$ দেওয়া আছে, $y=\tan(x+y)$\\$x-\text{এর সাপেক্ষে অন্তরীকরণ করে পাই,}$\\$\frac{dy}{dx}=\sec^2(x+y)\frac{d}{dx}(x+y)=\sec^2(x+y)\left(1+\frac{dy}{dx}\right)$\\$\therefore \frac{dy}{dx}-\sec^2(x+y)\frac{dy}{dx}=\sec^2(x+y)$\\$\therefore \{1-\sec^2(x+y)\}\frac{dy}{dx}=1+\tan^2(x+y)$\\$\therefore -\tan^2(x+y)\frac{dy}{dx}=1+y^2$\\$\therefore -y^2\frac{dy}{dx}=1+y^2$\\$\therefore\frac{dy}{dx}=-\left(1+\frac{1}{y^2}\right)\ (Ans.)$

**Final answer:** $-\left(1+\frac{1}{y^2}\right)$

## ID 1292

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $y=\sin(x+y)^2$

**Solution:** $(ii)$ যদি, $y=\sin(x+y)^2$\\$x-\text{এর সাপেক্ষে অন্তরীকরণ করে পাই,}$\\$\frac{dy}{dx}=\cos(x+y)^2\cdot2(x+y)\left(1+\frac{dy}{dx}\right)$\\$=2(x+y)\cos(x+y)^2+2(x+y)\cos(x+y)^2\frac{dy}{dx}$\\$\therefore \{1-2(x+y)\cos(x+y)^2\}\frac{dy}{dx}=2(x+y)\cos(x+y)^2$\\$\therefore\frac{dy}{dx}=\frac{2(x+y)\cos(x+y)^2}{1-2(x+y)\cos(x+y)^2}$\\$=\frac{2(x+y)\sqrt{1-y^2}}{1-2(x+y)\sqrt{1-y^2}}\ (Ans.)$

**Final answer:** $\frac{2(x+y)\sqrt{1-y^2}}{1-2(x+y)\sqrt{1-y^2}}$

## ID 1293

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $x\cos y=\sin(x+y)$

**Solution:** $(iii)$ দেওয়া আছে, $x\cos y=\sin(x+y)$\\$x-\text{এর সাপেক্ষে অন্তরীকরণ করে পাই,}$\\$\cos y-x\sin y\frac{dy}{dx}=\cos(x+y)\frac{d}{dx}(x+y)$\\$\cos y-x\sin y\frac{dy}{dx}=\cos(x+y)\left(1+\frac{dy}{dx}\right)$\\$\therefore -\{x\sin y+\cos(x+y)\}\frac{dy}{dx}=\cos(x+y)-\cos y$\\$\therefore\frac{dy}{dx}=\frac{\cos y-\cos(x+y)}{x\sin y+\cos(x+y)}\ (Ans.)$

**Final answer:** $\frac{\cos y-\cos(x+y)}{x\sin y+\cos(x+y)}$

## ID 1294

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $x^2+y^2=\sin(xy)$

**Solution:** $(iv)\ x^2+y^2=\sin(xy)$\\$x-\text{এর সাপেক্ষে অন্তরীকরণ করে পাই,}$\\$2x+2y\frac{dy}{dx}=\cos(xy)\frac{d}{dx}(xy)$\\$2x+2y\frac{dy}{dx}=\cos(xy)\left(x\frac{dy}{dx}+y\right)$\\$\therefore \{2y-x\cos(xy)\}\frac{dy}{dx}=-2x+y\cos(xy)$\\$\therefore\frac{dy}{dx}=\frac{y\cos(xy)-2x}{2y-x\cos(xy)}\ (Ans.)$

**Final answer:** $\frac{y\cos(xy)-2x}{2y-x\cos(xy)}$

## ID 1295

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $x=y\ln(xy)$

**Solution:** $(v)$ দেওয়া আছে, $x=y\ln(xy)$\\$1=\frac{y}{x}+\ln x\frac{dy}{dx}+\frac{y}{y}\frac{dy}{dx}+\ln y\frac{dy}{dx}$\\$\therefore 1-\frac{y}{x}=(\ln xy+1)\frac{dy}{dx}$\\$\therefore \frac{x-y}{x}=\left(\frac{x}{y}+1\right)\frac{dy}{dx}$\\$\therefore\frac{dy}{dx}=\frac{y(x-y)}{x(x+y)}\ (Ans.)$

**Final answer:** $\frac{y(x-y)}{x(x+y)}$

## ID 1296

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $\ln(xy)=x+y$

**Solution:** $(vi)$ দেওয়া আছে, $\ln(xy)=x+y$\\$\therefore \ln x+\ln y-x-y=0$\\$x-\text{এর সাপেক্ষে অন্তরীকরণ করে পাই,}$\\$\frac{1}{x}+\frac{1}{y}\frac{dy}{dx}-1-\frac{dy}{dx}=0$\\$\therefore \left(\frac{1}{y}-1\right)\frac{dy}{dx}=1-\frac{1}{x}$\\$\therefore\frac{dy}{dx}=\frac{y(x-1)}{x(1-y)}\ (Ans.)$

**Final answer:** $\frac{y(x-1)}{x(1-y)}$

## ID 1297

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $e^{xy}-4xy=2$

**Solution:** $(vii)$ দেওয়া আছে, $e^{xy}-4xy=2$\\$x-\text{এর সাপেক্ষে অন্তরীকরণ করে পাই,}$\\$e^{xy}\frac{d}{dx}(xy)-4y-4x\frac{dy}{dx}=0$\\$e^{xy}\left(x\frac{dy}{dx}+y\right)-4y-4x\frac{dy}{dx}=0$\\$x(e^{xy}-4)\frac{dy}{dx}=4y-ye^{xy}$\\$\therefore\frac{dy}{dx}=-\frac{y}{x}\ (Ans.)$

**Final answer:** $-\frac{y}{x}$

## ID 1298

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $x^2=5y^2+\sin y$

**Solution:** $(viii)\ x^2=5y^2+\sin y$\\$x-\text{এর সাপেক্ষে অন্তরীকরণ করে পাই,}$\\$2x=10y\frac{dy}{dx}+\cos y\frac{dy}{dx}$\\$\therefore\frac{dy}{dx}=\frac{2x}{10y+\cos y}\ (Ans.)$

**Final answer:** $\frac{2x}{10y+\cos y}$

## ID 1299

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $\tan y=\sin x$

**Solution:** $(ix)$ দেওয়া আছে, $\tan y=\sin x$\\$\therefore y=\tan^{-1}\sin x$\\$\therefore\frac{dy}{dx}=\frac{1}{1+\sin^2x}\cos x=\frac{\cos x}{1+\sin^2x}\ (Ans.)$

**Final answer:** $\frac{\cos x}{1+\sin^2x}$

## ID 1300

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $(\cos x)^y=(\sin y)^x$

**Solution:** $3.(i)\ (\cos x)^y=(\sin y)^x$\\$\therefore \ln(\cos x)^y=\ln(\sin y)^x$ [উভয় পাশে ln নিয়ে]\\$y\ln(\cos x)=x\ln(\sin y)$\\$\frac{dy}{dx}\ln(\cos x)+y(-\tan x)=\ln(\sin y)+x\cot y\frac{dy}{dx}$\\$\therefore\frac{dy}{dx}\{\ln(\cos x)-x\cot y\}=\ln(\sin y)+y\tan x$\\$\therefore\frac{dy}{dx}=\frac{\ln(\sin y)+y\tan x}{\ln(\cos x)-x\cot y}\ (Ans.)$

**Final answer:** $\frac{\ln(\sin y)+y\tan x}{\ln(\cos x)-x\cot y}$

## ID 1301

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $(\sec x)^y=(\tan y)^x$

**Solution:** $(ii)$ দেওয়া আছে, $(\sec x)^y=(\tan y)^x$\\$\therefore \ln(\sec x)^y=\ln(\tan y)^x$ [উভয় পাশে ln নিয়ে]\\$y\ln(\sec x)=x\ln(\tan y)$\\$\frac{dy}{dx}\ln(\sec x)+y\tan x=\ln(\tan y)+x\cot y\sec^2y\frac{dy}{dx}$\\$\therefore \{\ln(\sec x)-x\cot y\sec^2y\}\frac{dy}{dx}=\ln(\tan y)-y\tan x$\\$\therefore\frac{dy}{dx}=\frac{\ln(\tan y)-y\tan x}{\ln(\sec x)-x\cot y\sec^2y}\ (Ans.)$

**Final answer:** $\frac{\ln(\tan y)-y\tan x}{\ln(\sec x)-x\cot y\sec^2y}$

## ID 1302

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $x^yy^x=1$

**Solution:** $(iii)$ দেওয়া আছে, $x^yy^x=1$\\$\therefore \ln(x^yy^x)=\ln1$ [উভয় পাশে ln নিয়ে]\\$y\ln x+x\ln y=0$\\$\frac{dy}{dx}\ln x+\frac{y}{x}+\ln y+\frac{x}{y}\frac{dy}{dx}=0$\\$\therefore\frac{dy}{dx}=-\frac{\ln y+\frac{y}{x}}{\ln x+\frac{x}{y}}=-\frac{y(x\ln y+y)}{x(y\ln x+x)}\ (Ans.)$

**Final answer:** $-\frac{y(x\ln y+y)}{x(y\ln x+x)}$

## ID 1303

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $x^my^n=(x-y)^{m+n}$

**Solution:** $(iv)$ দেওয়া আছে, $x^my^n=(x-y)^{m+n}$\\$m\ln x+n\ln y=(m+n)\ln(x-y)$\\$\frac{m}{x}+\frac{n}{y}\frac{dy}{dx}=\frac{m+n}{x-y}\left(1-\frac{dy}{dx}\right)$\\$\therefore\frac{dy}{dx}=\frac{y}{x}\ (Ans.)$

**Final answer:** $\frac{y}{x}$

## ID 1304

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $x^y=e^{x-y}$

**Solution:** $(v)$ দেওয়া আছে, $x^y=e^{x-y}$\\$\therefore \ln x^y=\ln e^{x-y}$ [উভয় পাশে ln নিয়ে]\\$y\ln x=x-y$\\$\therefore y(1+\ln x)=x$\\$\therefore y=\frac{x}{1+\ln x}$\\$\therefore\frac{dy}{dx}=\frac{\ln x}{(1+\ln x)^2}\ (Ans.)$

**Final answer:** $\frac{\ln x}{(1+\ln x)^2}$

## ID 1305

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $y+x=x^{-y}$

**Solution:** $(vi)\ y+x=x^{-y}$\\$\therefore y+x=e^{-y\ln x}$\\$x-\text{এর সাপেক্ষে অন্তরীকরণ করে পাই,}$\\$\frac{dy}{dx}+1=x^{-y}\left[-\frac{y}{x}-\ln x\frac{dy}{dx}\right]$\\$\Rightarrow (1+x^{-y}\ln x)\frac{dy}{dx}=-1-yx^{-y-1}$\\$\therefore\frac{dy}{dx}=\frac{-1-yx^{-y-1}}{1+x^{-y}\ln x}\ (Ans.)$

**Final answer:** $\frac{-1-yx^{-y-1}}{1+x^{-y}\ln x}$

## ID 1306

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $e^y=x^{x-y}$

**Solution:** $(vii)\ e^y=x^{x-y}\Rightarrow y=\ln x^{x-y}=(x-y)\ln x$\\$x-\text{এর সাপেক্ষে অন্তরীকরণ করে পাই,}$\\$\frac{dy}{dx}=(x-y)\frac{1}{x}+\left(1-\frac{dy}{dx}\right)\ln x$\\$\Rightarrow (1+\ln x)\frac{dy}{dx}=1-\frac{y}{x}+\ln x$\\$\therefore\frac{dy}{dx}=1-\frac{y}{x(1+\ln x)}\ (Ans.)$

**Final answer:** $1-\frac{y}{x(1+\ln x)}$

## ID 1307

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $xy+y=\sin^{-1}\frac{y}{x}$

**Solution:** $4.(i)$ দেওয়া আছে, $xy+y=\sin^{-1}\frac{y}{x}$\\$\therefore \sin(xy+y)=\frac{y}{x}$\\$x-\text{এর সাপেক্ষে অন্তরীকরণ করে পাই,}$\\$\cos(xy+y)\left(x\frac{dy}{dx}+y+\frac{dy}{dx}\right)=\frac{x\frac{dy}{dx}-y}{x^2}$\\$x^2\cos(xy+y)\{(1+x)\frac{dy}{dx}+y\}=x\frac{dy}{dx}-y$\\$\therefore \{(x^2+x^3)\cos(xy+y)-x\}\frac{dy}{dx}=-x^2y\cos(xy+y)-y$\\$\therefore\frac{dy}{dx}=\frac{-x^2y\cos(xy+y)-y}{(x^2+x^3)\cos(xy+y)-x}\ (Ans.)$

**Final answer:** $\frac{-x^2y\cos(xy+y)-y}{(x^2+x^3)\cos(xy+y)-x}$

## ID 1308

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $x^y+y^x=a^b$

**Solution:** $(ii)$ দেওয়া আছে, $x^y+y^x=a^b$\\$\text{ধরি,} u=x^y\ \text{ও}\ v=y^x$\\$u=x^y\Rightarrow \ln u=y\ln x\Rightarrow \frac{du}{dx}=x^y\left(\frac{y}{x}+\ln x\frac{dy}{dx}\right)$\\$v=y^x\Rightarrow \ln v=x\ln y\Rightarrow \frac{dv}{dx}=y^x\left(\frac{x}{y}\frac{dy}{dx}+\ln y\right)$\\$\frac{du}{dx}+\frac{dv}{dx}=0$\\$\therefore\frac{dy}{dx}=\frac{-yx^{y-1}-y^x\ln y}{x^y\ln x+xy^{x-1}}\ (Ans.)$

**Final answer:** $\frac{-yx^{y-1}-y^x\ln y}{x^y\ln x+xy^{x-1}}$

## ID 1309

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $x=a\cos\theta,\ y=a\sin\theta$

**Solution:** $5.(i)\ x=a\cos\theta\quad\therefore\frac{dx}{d\theta}=-a\sin\theta$\\$y=a\sin\theta\quad\therefore\frac{dy}{d\theta}=a\cos\theta$\\$\therefore\frac{dy}{dx}=\frac{a\cos\theta}{-a\sin\theta}=-\cot\theta\ (Ans.)$

**Final answer:** $-\cot\theta$

## ID 1310

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $x=at^2,\ y=2at$

**Solution:** $(ii)\ x=at^2\quad\therefore\frac{dx}{dt}=2at$\\$y=2at\quad\therefore\frac{dy}{dt}=2a$\\$\therefore\frac{dy}{dx}=\frac{2a}{2at}=\frac{1}{t}\ (Ans.)$

**Final answer:** $\frac{1}{t}$

## ID 1311

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $x=e^t\cos t,\ y=e^t\sin t$

**Solution:** $(iii)\ x=e^t\cos t\quad\therefore\frac{dx}{dt}=e^t(-\sin t)+e^t\cos t$\\$y=e^t\sin t\quad\therefore\frac{dy}{dt}=e^t\cos t+e^t\sin t$\\$\therefore\frac{dy}{dx}=\frac{e^t(\cos t+\sin t)}{e^t(\cos t-\sin t)}=\frac{\cos t+\sin t}{\cos t-\sin t}\ (Ans.)$

**Final answer:** $\frac{\cos t+\sin t}{\cos t-\sin t}$

## ID 1312

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $x=a(\theta-\sin\theta),\ y=a(1-\cos\theta)$

**Solution:** $(iv)\ x=a(\theta-\sin\theta)\quad\therefore\frac{dx}{d\theta}=a(1-\cos\theta)$\\$y=a(1-\cos\theta)\quad\therefore\frac{dy}{d\theta}=a\sin\theta$\\$\therefore\frac{dy}{dx}=\frac{\sin\theta}{1-\cos\theta}=\cot\frac{\theta}{2}\ (Ans.)$

**Final answer:** $\cot\frac{\theta}{2}$

## ID 1313

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $x=\frac{3at}{1+t^3},\ y=\frac{3at^2}{1+t^3}$

**Solution:** $(v)\ x=\frac{3at}{1+t^3}$\\$\frac{dx}{dt}=\frac{(1+t^3)3a-3at\cdot3t^2}{(1+t^3)^2}=\frac{3a(1-2t^3)}{(1+t^3)^2}$\\$y=\frac{3at^2}{1+t^3}$\\$\frac{dy}{dt}=\frac{(1+t^3)6at-3at^2\cdot3t^2}{(1+t^3)^2}=\frac{3at(2-t^3)}{(1+t^3)^2}$\\$\therefore\frac{dy}{dx}=\frac{3at(2-t^3)}{(1+t^3)^2}\cdot\frac{(1+t^3)^2}{3a(1-2t^3)}=\frac{t(2-t^3)}{1-2t^3}\ (Ans.)$\\$\text{বিকল্প সমাধান:}\ x^2+y^2=3axy$\\$\therefore\frac{dy}{dx}=\frac{ay-x^2}{xy-ax}\ (Ans.)$

**Final answer:** $\frac{t(2-t^3)}{1-2t^3}$

## ID 1314

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $x=\frac{a\cos t}{t},\ y=\frac{a\sin t}{t}$

**Solution:** $(vi)\ x=\frac{a\cos t}{t}\quad\therefore\frac{dx}{dt}=\frac{-at\sin t-a\cos t}{t^2}$\\$y=\frac{a\sin t}{t}\quad\therefore\frac{dy}{dt}=\frac{at\cos t-a\sin t}{t^2}$\\$\therefore\frac{dy}{dx}=\frac{at\cos t-a\sin t}{-at\sin t-a\cos t}=\frac{\sin t-t\cos t}{t\sin t+\cos t}\ (Ans.)$

**Final answer:** $\frac{\sin t-t\cos t}{t\sin t+\cos t}$

## ID 1315

**Question:** অব্যক্ত ফাংশনের $dy/dx$ নির্ণয় করো। $x=a(\cos t+t\sin t),\ y=a(\sin t-t\cos t)$

**Solution:** $(vii)\ x=a(\cos t+t\sin t)$\\$\therefore\frac{dx}{dt}=a(-\sin t+\sin t+t\cos t)=at\cos t$\\$y=a(\sin t-t\cos t)$\\$\therefore\frac{dy}{dt}=a(\cos t-\cos t+t\sin t)=at\sin t$\\$\therefore\frac{dy}{dx}=\frac{at\sin t}{at\cos t}=\tan t\ (Ans.)$

**Final answer:** $\tan t$

## ID 1316

**Question:** $\frac{d^n}{dx^n}(\cos ax)$

**Solution:** $9.(i)$ যদি, $y=\cos ax$\\ x এর সাপেক্ষে পর্যায়ক্রমিক অন্তরীকরণ করে,\\$y_1=-a\sin ax=a\cos\left(\frac{\pi}{2}+ax\right)$\\$y_2=-a^2\cos ax=a^2\cos\left(\frac{2\pi}{2}+ax\right)$\\$y_3=a^3\sin ax=a^3\cos\left(\frac{3\pi}{2}+ax\right)$\\$y_4=a^4\cos ax=a^4\cos\left(\frac{4\pi}{2}+ax\right)$\\$\therefore y_n=a^n\cos\left(\frac{n\pi}{2}+ax\right)\ (Ans.)$

**Final answer:** $a^n\cos\left(\frac{n\pi}{2}+ax\right)$

## ID 1317

**Question:** $\frac{d^n}{dx^n}\left(\frac{1}{x}\right)$

**Solution:** $(ii)$ যদি, $y=\frac{1}{x}=x^{-1}$\\$\therefore y_1=(-1)x^{-2}$\\$\therefore y_2=(-1)(-2)x^{-3}=(-1)^2 2!x^{-3}$\\$\therefore y_3=(-1)(-2)(-3)x^{-4}=(-1)^3 3!x^{-(3+1)}$\\$\therefore y_n=(-1)^n n!x^{-(n+1)}$\\$\therefore y_n=\frac{(-1)^n n!}{x^{n+1}}\ (Ans.)$

**Final answer:** $\frac{(-1)^n n!}{x^{n+1}}$

## ID 1318

**Question:** $\frac{d^n}{dx^n}(2\sin3x\cos2x)$

**Solution:** $(iii)$ যদি, $y=2\sin3x\cos2x=\sin5x+\sin x$\\ x এর সাপেক্ষে পর্যায়ক্রমিক অন্তরীকরণ করে,\\$\therefore y_1=5\cos5x+\cos x=5\sin\left(\frac{\pi}{2}+5x\right)+\sin\left(\frac{\pi}{2}+x\right)$\\$y_2=-5^2\sin5x-\sin x=5^2\sin\left(\frac{2\pi}{2}+5x\right)+\sin\left(\frac{2\pi}{2}+x\right)$\\$y_3=-5^3\cos5x-\cos x=5^3\sin\left(\frac{3\pi}{2}+5x\right)+\sin\left(\frac{3\pi}{2}+x\right)$\\$y_4=5^4\sin5x+\sin x=5^4\sin\left(\frac{4\pi}{2}+5x\right)+\sin\left(\frac{4\pi}{2}+x\right)$\\$\therefore y_n=5^n\sin\left(\frac{n\pi}{2}+5x\right)+\sin\left(\frac{n\pi}{2}+x\right)\ (Ans.)$

**Final answer:** $5^n\sin\left(\frac{n\pi}{2}+5x\right)+\sin\left(\frac{n\pi}{2}+x\right)$

## ID 1319

**Question:** $\frac{d^n}{dx^n}(4\sin^3x)$

**Solution:** $(iv)$ যদি, $y=4\sin^3x=(3\sin x-\sin3x)$\\ x এর সাপেক্ষে পর্যায়ক্রমিক অন্তরীকরণ করে,\\$\therefore y_1=3\cos x-3\cos3x=3\sin\left(\frac{\pi}{2}+x\right)-3\sin\left(\frac{\pi}{2}+3x\right)$\\$y_2=3\cos\left(\frac{\pi}{2}+x\right)-3^2\cos\left(\frac{\pi}{2}+3x\right)$\\$=3\sin\left(\frac{2\pi}{2}+x\right)-3^2\sin\left(\frac{2\pi}{2}+3x\right)$\\$y_3=3\sin\left(\frac{3\pi}{2}+x\right)-3^3\sin\left(\frac{3\pi}{2}+3x\right)$\\$\therefore y_n=3\sin\left(\frac{n\pi}{2}+x\right)-3^n\sin\left(\frac{n\pi}{2}+3x\right)\ (Ans.)$

**Final answer:** $3\sin\left(\frac{n\pi}{2}+x\right)-3^n\sin\left(\frac{n\pi}{2}+3x\right)$

## ID 1320

**Question:** $\frac{d^n}{dx^n}(\cos^3x)$

**Solution:** $(v)$ যদি, $y=\cos^3x=\frac{1}{4}[\cos3x+3\cos x]$\\ x এর সাপেক্ষে পর্যায়ক্রমিক অন্তরীকরণ করে,\\$\therefore y_1=\frac{1}{4}[-3\sin3x-3\sin x]$\\$=\frac{1}{4}\left[3\cos\left(\frac{\pi}{2}+3x\right)+3\cos\left(\frac{\pi}{2}+x\right)\right]$\\$y_2=\frac{1}{4}\left[3^2\cos\left(\frac{2\pi}{2}+3x\right)+3\cos\left(\frac{2\pi}{2}+x\right)\right]$\\$y_3=\frac{1}{4}\left[3^3\cos\left(\frac{3\pi}{2}+3x\right)+3\cos\left(\frac{3\pi}{2}+x\right)\right]$\\$\therefore y_n=\frac{1}{4}\left[3^n\cos\left(\frac{n\pi}{2}+3x\right)+3\cos\left(\frac{n\pi}{2}+x\right)\right]\ (Ans.)$

**Final answer:** $\frac{1}{4}\left[3^n\cos\left(\frac{n\pi}{2}+3x\right)+3\cos\left(\frac{n\pi}{2}+x\right)\right]$

## ID 1321

**Question:** $\frac{d^n}{dx^n}(\ln x)$

**Solution:** $(vi)$ $y=\ln x$\\$y_1=\frac{1}{x}=x^{-1}$\\$y_2=(-1)x^{-2}$\\$y_3=(-1)(-2)x^{-3}=(-1)^2 2!x^{-3}$\\$y_4=(-1)^3 3!x^{-4}$\\$\therefore y_n=(-1)^{n-1}(n-1)!x^{-n}$\\$\therefore y_n=\frac{(-1)^{n-1}(n-1)!}{x^n}\ (Ans.)$

**Final answer:** $\frac{(-1)^{n-1}(n-1)!}{x^n}$

## ID 1322

**Question:** $\frac{d^n}{dx^n}(e^{3x}\sin^2x)$

**Solution:** $(vii)$ $y=e^{3x}\sin^2x=\frac{1}{2}e^{3x}(1-\cos2x)$\\$=\frac{1}{2}e^{3x}-\frac{1}{2}e^{3x}\cos2x$\\ For $e^{3x}\cos2x$, one differentiation gives $e^{3x}(3\cos2x-2\sin2x)=\sqrt{13}e^{3x}\cos(2x+\theta)$, where $\theta=\tan^{-1}\frac{2}{3}$.\\ Thus after repeated differentiation,\\$\therefore y_n=\frac{1}{2}e^{3x}\{3^n-(\sqrt{13})^n\cos(2x+n\theta)\}$\\ where $\theta=\tan^{-1}\frac{2}{3}\ (Ans.)$

**Final answer:** $\frac{1}{2}e^{3x}\{3^n-(\sqrt{13})^n\cos(2x+n\theta)\},\ \theta=\tan^{-1}\frac{2}{3}$

## ID 1323

**Question:** সরলরেখায় চলমান কোনো কণার $t$ সেকেন্ডে অতিক্রান্ত দূরত্ব $s=\frac{1}{2}t^3+t^2+4t$ সম্পর্কের দ্বারা প্রকাশিত। গতি শুরুর 5 সেকেন্ড পরে কণাটির বেগ ও ত্বরণ নির্ণয় কর।

**Solution:** দেওয়া আছে, $s=\frac{1}{2}t^3+t^2+4t$\\$\therefore v=\frac{ds}{dt}=\frac{3}{2}t^2+2t+4$\\$t=5$ সেকেন্ড হলে, $v=\frac{3}{2}(5)^2+2(5)+4=\frac{103}{2}$ একক/সেকেন্ড।\\আবার, $f=\frac{dv}{dt}=3t+2$\\$t=5$ সেকেন্ড হলে, $f=3\cdot5+2=17$ একক/সেকেন্ড$^2$।

**Final answer:** $v=\frac{103}{2}$ একক/সেকেন্ড এবং $f=17$ একক/সেকেন্ড$^2$

## ID 1324

**Question:** একটি ট্রেন $t$ সেকেন্ডে $3t+\frac{1}{8}t^2$ মিটার অতিক্রম করে। 5 মিনিট পর তার বেগ কত হবে।

**Solution:** আমরা পাই, $s=3t+\frac{1}{8}t^2$ মিটার\\$\therefore v=\frac{ds}{dt}=3+\frac{1}{8}\cdot2t=3+\frac{1}{4}t$\\$5$ মিনিট $=5\times60=300$ সেকেন্ড।\\$\therefore v=3+\frac{1}{4}\cdot300=3+75=78$ মিটার/সেকেন্ড।

**Final answer:** $78$ মিটার/সেকেন্ড

## ID 1325

**Question:** একটি কণা সরলরেখায় এমনভাবে চলে যেন $t$ সময়ে তার অতিক্রান্ত দূরত্ব $s=\sqrt{t}$। দেখাও যে, কণাটির ত্বরণ ঋণাত্মক এবং বেগের ঘনফলের সাথে সমানুপাতিক।

**Solution:** এখানে, $s=\sqrt{t}$\\$\therefore v=\frac{ds}{dt}=\frac{1}{2t^{\frac{1}{2}}}=\frac{1}{2}t^{-\frac{1}{2}}$\\$\therefore v^3=\frac{1}{8t^{\frac{3}{2}}}$\\আবার, $f=\frac{dv}{dt}=\frac{1}{2}\left(-\frac{1}{2}\right)t^{-\frac{3}{2}}=-\frac{1}{4t^{\frac{3}{2}}}$\\$\therefore f=-2v^3$\\সুতরাং ত্বরণ ঋণাত্মক এবং বেগের ঘনফলের সাথে সমানুপাতিক।

**Final answer:** $f=-2v^3$; অতএব ত্বরণ ঋণাত্মক এবং $v^3$ এর সমানুপাতিক

## ID 1326

**Question:** সরলরৈখিক পথে চলমান কোনো কণা $t$ সময়ে $s=at^2+bt+c$ দূরত্ব অতিক্রম করে, যেখানে $a,b,c$ ধ্রুবক। $t$ সময়ে কণার বেগ $v$ হলে, দেখাও যে, $v^2-b^2=4a(s-c)$।

**Solution:** দেওয়া আছে, $s=at^2+bt+c$\\$\therefore v=\frac{ds}{dt}=2at+b$\\$\therefore v^2=4a^2t^2+4abt+b^2$\\$\therefore v^2-b^2=4a(at^2+bt)=4a(s-c)$

**Final answer:** প্রমাণিত, $v^2-b^2=4a(s-c)$

## ID 1327

**Question:** যদি একটি কণা এমনভাবে চলে যে এর দূরত্ব, অতিবাহিত সময়ের বর্গের সমানুপাতিক, তবে দেখাও যে, বেগ সময়ের সমানুপাতিক এবং বেগ পরিবর্তনের হার ধ্রুবক।

**Solution:** মনে করি, দূরত্ব $s$ সময় $t$ এর বর্গের সমানুপাতিক।\\$\therefore s\propto t^2$\\বা, $s=kt^2$, যেখানে $k$ সমানুপাতিক ধ্রুবক।\\$\therefore v=\frac{ds}{dt}=2kt$\\অতএব, $v\propto t$।\\আবার, $f=\frac{dv}{dt}=2k$, যা ধ্রুবক।

**Final answer:** $v\propto t$ এবং $\frac{dv}{dt}=2k$, অর্থাৎ ধ্রুবক

## ID 1328

**Question:** একটি বস্তুর গতির সমীকরণ $s=t^3+\frac{1}{t^3}$ হলে দেখাও যে, এর ত্বরণ সর্বদাই ধনাত্মক এবং $t=10$ হলে এর গতিবেগ নির্ণয় কর।

**Solution:** গতির সমীকরণ $s=t^3+\frac{1}{t^3}$\\$\therefore t$ সময়ে গতিবেগ, $v=\frac{ds}{dt}=3t^2-\frac{3}{t^4}$\\যখন $t=10$, গতিবেগ $=300-\frac{3}{10^4}=299.999$ একক প্রায়।\\আবার $t$ সময়ে ত্বরণ, $\frac{d^2s}{dt^2}=6t+\frac{12}{t^5}>0$; $t>0$।\\$\therefore$ ত্বরণের মান সব সময় ধনাত্মক।

**Final answer:** $t=10$ হলে গতিবেগ $=300-\frac{3}{10^4}=299.999$ একক প্রায়; ত্বরণ সর্বদাই ধনাত্মক

## ID 1329

**Question:** একটি কণা সরলপথে এমনভাবে চলে যেন $t$ সময়ে তার অতিক্রান্ত দূরত্ব $s=\sqrt{2t}$ হয়। দেখাও যে, কণাটির ত্বরণ বেগের ঘনফলের সাথে সমানুপাতিক।

**Solution:** এখানে, $s=\sqrt{2t}=\sqrt{2}\,t^{\frac{1}{2}}$\\$\therefore$ কণাটির বেগ $v=\frac{ds}{dt}=\frac{1}{\sqrt{2}}t^{-\frac{1}{2}}$\\ত্বরণ, $\frac{d^2s}{dt^2}=-\frac{1}{2\sqrt{2}}t^{-\frac{3}{2}}$\\$=-\left(\frac{1}{\sqrt{2}}t^{-\frac{1}{2}}\right)^3$\\$=-(\text{বেগ})^3$\\সুতরাং, কণাটির ত্বরণ বেগের ঘনফলের সাথে সমানুপাতিক।

**Final answer:** $f=-v^3$; অতএব ত্বরণ বেগের ঘনফলের সাথে সমানুপাতিক

## ID 1330

**Question:** একটি পুকুরের একটি বৃত্তাকার ঢেউ এর পরিধির বৃদ্ধির হার $a$ ফুট/সেকেন্ড। দেখাও যে, এর ব্যাসার্ধ বৃদ্ধির হার $a/2\pi$ ফুট/সেকেন্ড।

**Solution:** মনে করি, $t$ সেকেন্ডে প্রদত্ত বৃত্তাকার ঢেউ এর ব্যাসার্ধ $r$ ফুট এবং পরিধি $S$ ফুট।\\তাহলে, $S=2\pi r$\\উভয়পক্ষ $t$ এর সাপেক্ষে অন্তরীকরণ করে পাই, $\frac{dS}{dt}=2\pi\frac{dr}{dt}$\\প্রশ্নমতে, $\frac{dS}{dt}=a$।\\$\therefore a=2\pi\frac{dr}{dt}$ বা, $\frac{dr}{dt}=\frac{a}{2\pi}$\\$\therefore$ ব্যাসার্ধ বৃদ্ধির হার $=\frac{a}{2\pi}$ ফুট/সেকেন্ড।

**Final answer:** ব্যাসার্ধ বৃদ্ধির হার $=\frac{a}{2\pi}$ ফুট/সেকেন্ড

## ID 1331

**Question:** $(0,1)$ ব্যবধিতে $f(x)=3+2x-x^2$ ফাংশনের জন্য গড়মান উপপাদ্যটির সত্যতা যাচাই কর।

**Solution:** গড়মান উপপাদ্য হতে আমরা জানি, $(b-a)f'(c)=f(b)-f(a)$, যেখানে $a<c<b$।\\$f(x)=3+2x-x^2$\\$f'(x)=2-2x$\\এখানে, $a=0$, $b=1$, $0<c<1$।\\$f(0)=3$ এবং $f(1)=4$\\এখন, $(b-a)f'(c)=f(b)-f(a)$\\বা, $(1-0)f'(c)=4-3$\\বা, $f'(c)=1$\\অতএব, $2-2c=1$, অর্থাৎ $c=\frac{1}{2}$।\\যেহেতু $0<\frac{1}{2}<1$, অর্থাৎ $0<c<1$, সুতরাং $(0,1)$ ব্যবধির মধ্যে অবস্থান করে।\\গড়মান উপপাদ্যটির সত্যতা প্রমাণিত হলো।

**Final answer:** $c=\frac{1}{2}$; গড়মান উপপাদ্যটির সত্যতা প্রমাণিত

## ID 1332

**Question:** উল্লিখিত ব্যবধিতে নিম্নলিখিত ফাংশনগুলির গড়মান উপপাদ্যের সত্যতা যাচাই কর। (i) $f(x)=(x-1)(x-2)(x-3); [0,4]$

**Solution:** দেওয়া আছে, $f(x)=(x-1)(x-2)(x-3)=x^3-6x^2+11x-6$\\$\therefore f'(x)=3x^2-12x+11$\\$f(x)$ ফাংশন বহুপদী হওয়ায় $x$ এর সকল মানের জন্য অবিচ্ছিন্ন। কাজেই $[0,4]$ ব্যবধিতে $f(x)$ ফাংশন অবিচ্ছিন্ন।\\আবার, সকল $x\in(0,4)$ এর জন্য $f(x)$ বিদ্যমান বলে $f(x)$ ফাংশন $(0,4)$ ব্যবধিতে অন্তরীকরণযোগ্য।\\গড়মান উপপাদ্যের শর্ত পূরণ করে, কাজেই অন্ততপক্ষে একটি $c\in(0,4)$ পাওয়া যাবে যাতে,\\$f'(c)=\frac{f(4)-f(0)}{4-0}$\\বা, $3c^2-12c+11=3$\\বা, $3c^2-12c+8=0$\\$\therefore c=2\pm\frac{2}{\sqrt{3}}$\\স্পষ্টত $2-\frac{2}{\sqrt{3}}, 2+\frac{2}{\sqrt{3}}\in(0,4)$।\\সুতরাং ল্যাগরাঞ্জের গড়মান উপপাদ্যের সত্যতা প্রমাণিত হলো।

**Final answer:** $c=2-\frac{2}{\sqrt{3}},\ 2+\frac{2}{\sqrt{3}}$; গড়মান উপপাদ্যের সত্যতা প্রমাণিত

## ID 1333

**Question:** উল্লিখিত ব্যবধিতে নিম্নলিখিত ফাংশনগুলির গড়মান উপপাদ্যের সত্যতা যাচাই কর। (ii) $f(x)=\sqrt{x^2-4}; [2,4]$

**Solution:** প্রদত্ত ফাংশন: $f(x)=\sqrt{x^2-4}$\\$\therefore f'(x)=\frac{2x}{2\sqrt{x^2-4}}=\frac{x}{\sqrt{x^2-4}}$\\প্রত্যেক $x\in[2,4]$ এর জন্য $f(x)$ এর একক ও নির্দিষ্ট মান বিদ্যমান, কাজেই $f(x)$ ফাংশন $[2,4]$ বদ্ধ ব্যবধিতে অবিচ্ছিন্ন।\\আবার, প্রত্যেক $x\in(2,4)$ এর জন্য $f(x)$ বিদ্যমান, কাজেই $f(x)$ ফাংশন $(2,4)$ খোলা ব্যবধিতে অন্তরীকরণযোগ্য।\\সুতরাং $f(x)$ ফাংশন ল্যাগরাঞ্জের গড়মান উপপাদ্যের সকল শর্ত পূরণ করে।\\কাজেই অন্ততপক্ষে একটি $c\in(2,4)$ পাওয়া যাবে যেন,\\$f'(c)=\frac{f(4)-f(2)}{4-2}$\\বা, $\frac{c}{\sqrt{c^2-4}}=\frac{\sqrt{12}-0}{2}$\\বা, $\frac{c^2}{c^2-4}=3$\\$\therefore c^2=6$; যেহেতু $c\in(2,4)$, সুতরাং $c=\sqrt{6}$।\\সুতরাং ল্যাগরাঞ্জের গড়মান উপপাদ্যের সত্যতা প্রমাণিত হলো।

**Final answer:** $c=\sqrt{6}$; গড়মান উপপাদ্যের সত্যতা প্রমাণিত

## ID 1334

**Question:** উল্লিখিত ব্যবধিতে নিম্নলিখিত ফাংশনগুলির গড়মান উপপাদ্যের সত্যতা যাচাই কর। (iii) $f(x)=\ln x; [1,e]$

**Solution:** প্রদত্ত ফাংশন: $f(x)=\ln x$\\$\therefore f'(x)=\frac{1}{x}$\\যেহেতু $\ln x$ ফাংশনটি সকল $x>0$ এর জন্য অবিচ্ছিন্ন, কাজেই $f(x)$ ফাংশন $[1,e]$ বদ্ধ ব্যবধিতে অবিচ্ছিন্ন।\\আবার, প্রত্যেক $x\in(1,e)$ এর জন্য $f'(x)$ বিদ্যমান, কাজেই $f(x)$ ফাংশন $(1,e)$ ব্যবধিতে অন্তরীকরণযোগ্য।\\সুতরাং $f(x)$ ফাংশন ল্যাগরাঞ্জের গড়মান উপপাদ্যের সকল শর্ত পূরণ করে।\\কাজেই অন্ততপক্ষে একটি $c\in(1,e)$ বিদ্যমান যাতে,\\$f'(c)=\frac{f(e)-f(1)}{e-1}$\\বা, $\frac{1}{c}=\frac{\ln e-\ln1}{e-1}$\\বা, $\frac{1}{c}=\frac{1}{e-1}$\\$\therefore c=e-1$; যেহেতু $1<c<e$।\\সুতরাং গড়মান উপপাদ্যের সত্যতা প্রমাণিত হলো।

**Final answer:** $c=e-1$; গড়মান উপপাদ্যের সত্যতা প্রমাণিত

## ID 1335

**Question:** মধ্যবর্তী মান উপপাদ্য ব্যবহার করে দেখাও যে, নিম্নোক্ত সমীকরণগুলির উল্লিখিত ব্যবধিতে কমপক্ষে একটি করে সমাধান আছে। (i) $x^3-4x+1=0; [1,2]$

**Solution:** ধরি, $f(x)=x^3-4x+1$, যা একটি বহুপদী ফাংশন। তাই $f(x)$ একটি অবিচ্ছিন্ন ফাংশন।\\আবার, $f(1)=1^3-4\cdot1+1=-2$\\$f(2)=2^3-4\cdot2+1=1$\\$\therefore f(1)$ ও $f(2)$ বিপরীত চিহ্ন বিশিষ্ট।\\তাই $[1,2]$ ব্যবধিতে $f(x)$ এর কমপক্ষে একটি শূন্যস্থান বিদ্যমান।

**Final answer:** $[1,2]$ ব্যবধিতে কমপক্ষে একটি সমাধান আছে

## ID 1336

**Question:** মধ্যবর্তী মান উপপাদ্য ব্যবহার করে দেখাও যে, নিম্নোক্ত সমীকরণগুলির উল্লিখিত ব্যবধিতে কমপক্ষে একটি করে সমাধান আছে। (ii) $x^3+x^2-2x=1; [-1,1]$

**Solution:** $x^3+x^2-2x=1$ বা, $x^3+x^2-2x-1=0$\\ধরি, $f(x)=x^3+x^2-2x-1$, যা একটি বহুপদী ফাংশন। তাই $f(x)$ একটি অবিচ্ছিন্ন ফাংশন।\\আবার, $f(-1)=(-1)^3+(-1)^2-2(-1)-1=1$\\$f(1)=1^3+1^2-2\cdot1-1=-1$\\$\therefore f(-1)$ ও $f(1)$ বিপরীত চিহ্ন বিশিষ্ট।\\তাই $[-1,1]$ ব্যবধিতে $f(x)$ এর কমপক্ষে একটি শূন্যস্থান বিদ্যমান।

**Final answer:** $[-1,1]$ ব্যবধিতে কমপক্ষে একটি সমাধান আছে

## ID 1337

**Question:** মধ্যবর্তী মান উপপাদ্য ব্যবহার করে দেখাও যে, নিম্নোক্ত সমীকরণগুলির উল্লিখিত ব্যবধিতে কমপক্ষে একটি করে সমাধান আছে। (iii) $x^3-x-1=0; [1,2]$

**Solution:** ধরি, $f(x)=x^3-x-1$, যা একটি বহুপদী ফাংশন। তাই $f(x)$ একটি অবিচ্ছিন্ন ফাংশন।\\আবার, $f(1)=1^3-1-1=-1$\\$f(2)=2^3-2-1=5$\\$\therefore f(1)$ ও $f(2)$ বিপরীত চিহ্ন বিশিষ্ট।\\তাই $[1,2]$ ব্যবধিতে $f(x)$ এর কমপক্ষে একটি সমাধান বিদ্যমান।

**Final answer:** $[1,2]$ ব্যবধিতে কমপক্ষে একটি সমাধান আছে

## ID 1338

**Question:** যদি একটি সমবাহু ত্রিভুজের বাহুগুলো প্রতি সেকেন্ডে $\sqrt{3}$ সেমি. এবং এর ক্ষেত্রফল প্রতি সেকেন্ডে 12 বর্গ সেমি. পরিমাণ বৃদ্ধি পায়, তাহলে সমবাহু ত্রিভুজের বাহুর দৈর্ঘ্য নির্ণয় কর।

**Solution:** ধরি, সমবাহু ত্রিভুজের বাহুর দৈর্ঘ্য $x$ সেমি. এবং এর ক্ষেত্রফল $A$ বর্গ সেমি.।\\তাহলে, $A=\frac{\sqrt{3}}{4}x^2$\\বা, $\frac{dA}{dt}=\frac{\sqrt{3}}{4}\times2x\frac{dx}{dt}$\\প্রশ্নমতে, $\frac{dx}{dt}=\sqrt{3}$ এবং $\frac{dA}{dt}=12$।\\$\therefore 12=\frac{\sqrt{3}}{4}\times2x\times\sqrt{3}$\\বা, $3x=24$, অর্থাৎ $x=8$।\\$\therefore$ বাহুর দৈর্ঘ্য $8$ সেমি.।

**Final answer:** $8$ সেমি.

## ID 1339

**Question:** একটি আয়তাকার জমির একদিকে নদী ও অপর তিনদিকে একটি বৈদ্যুতিক বেড়া আছে। 800m তার দিয়ে জমির সর্বোচ্চ কতটুকু এলাকা আবদ্ধ করা যাবে এবং এর মাত্রা কি হবে।

**Solution:** এখানে, $x+2y=800$ বা, $x=800-2y$\\ধরি, $A=xy$\\$\therefore A=800y-2y^2$\\$\therefore \frac{dA}{dy}=800-4y$\\সর্বোচ্চ ক্ষেত্রফলের জন্য, $\frac{dA}{dy}=0$।\\অর্থাৎ, $800-4y=0$, তাই $y=200$ মিটার।\\$\therefore x=400$ মিটার।\\$\therefore A=400\times200=80000$ বর্গমিটার।

**Final answer:** $400$ মিটার ও $200$ মিটার; সর্বোচ্চ ক্ষেত্রফল $80000$ বর্গমিটার

## ID 1340

**Question:** রাতের বেলা একটি গাড়ি দক্ষিণ দিকে 8 কিমি./ঘণ্টা বেগে 30 মিনিট চলার পর পশ্চিম দিকে ঘুরে। একটি ফ্লাশলাইট গাড়িটিকে চিহ্নিত করতে যাত্রা শুরুর স্থানে লাগানো আছে। ফ্লাশলাইট কত কৌণিক গতিতে গাড়িটি ছাড়ার পর 1 ঘণ্টা ঘুরবে।

**Solution:** এখানে, $x=8t$।\\$\therefore \theta=\tan^{-1}\left(\frac{8t}{4}\right)=\tan^{-1}(2t)$\\$\therefore \frac{d\theta}{dt}=\frac{1}{1+4t^2}\times2$\\$t=\frac{1}{2}$ ঘণ্টা পর,\\$\therefore \frac{d\theta}{dt}=\frac{2}{1+4\left(\frac{1}{2}\right)^2}=1$ রেডিয়ান/ঘণ্টা।

**Final answer:** $1$ রেডিয়ান/ঘণ্টা

## ID 1341

**Question:** একটি বস্তুর সরণ $x(t)=\frac{t(3-2t)}{2}$। যে সময়ে বস্তুর বেগ ও সরণের সংখ্যামান সমান, তা নির্ণয় কর। বস্তুর সময়, বেগ ও সরণের সংখ্যামান সমান হওয়ার সময়ও নির্ণয় কর।

**Solution:** $x(t)=\frac{t(3-2t)}{2}$\\$\therefore v(t)=\frac{1}{2}(3-4t)$\\এখন, $|x(t)|=|v(t)|$ বা, $\left|\frac{t(3-2t)}{2}\right|=\left|\frac{1}{2}(3-4t)\right|$\\ধনাত্মক চিহ্ন নিয়ে, $3t-2t^2=3-4t$\\বা, $2t^2-7t+3=0$\\$\therefore t=3,\frac{1}{2}$\\ঋণাত্মক চিহ্ন নিয়ে, $3t-2t^2=-3+4t$\\বা, $2t^2+t-3=0$\\$\therefore t=1,-\frac{3}{2}$\\$t$ এর ঋণাত্মক মান গ্রহণযোগ্য নয়।\\$\therefore t=1,3,\frac{1}{2}$।\\আবার, $t=\frac{1}{2}$ হলে সরণের সংখ্যামান, $\left|x\left(\frac{1}{2}\right)\right|=\left|\frac{\frac{1}{2}(3-2\times\frac{1}{2})}{2}\right|=\frac{1}{2}$\\এবং বেগের সংখ্যামান, $\left|v\left(\frac{1}{2}\right)\right|=\left|\frac{1}{2}(3-4\times\frac{1}{2})\right|=\frac{1}{2}$।\\$\therefore$ বস্তুর সময়, বেগ ও সরণের সংখ্যামান সমান হওয়ার সময় $\frac{1}{2}$।

**Final answer:** $|x|=|v|$ হলে $t=\frac{1}{2},1,3$; সময়, বেগ ও সরণের সংখ্যামান সমান হলে $t=\frac{1}{2}$

## ID 1342

**Question:** 1 লিটার (1000 ঘন সেমি.) তরল ধারণ ক্ষমতা সম্পন্ন দুই প্রান্তে আবদ্ধ একটি খাড়া বৃত্তাকার সিলিন্ডার প্রয়োজন। সিলিন্ডারটির উচ্চতা ও ব্যাসার্ধ কিরূপ হলে সর্বাপেক্ষা কম ক্ষেত্রফল বিশিষ্ট টিন দিয়ে তা তৈরি করা সম্ভব।

**Solution:** আমরা জানি, $1000\text{ cm}^3=1\text{ dm}^3$।\\ধরি, সিলিন্ডারের উচ্চতা $h$ dm এবং ব্যাসার্ধ $r$ dm।\\$\therefore \pi r^2h=1$ বা, $h=\frac{1}{\pi r^2}$\\সিলিন্ডারের ক্ষেত্রফল, $A=2\pi r^2+2\pi rh$\\$=2\pi r^2+2\pi r\left(\frac{1}{\pi r^2}\right)=2\pi r^2+\frac{2}{r}$\\$\therefore \frac{dA}{dr}=4\pi r-\frac{2}{r^2}$\\$\therefore \frac{d^2A}{dr^2}=4\pi+\frac{4}{r^3}>0$; সর্বনিম্ন মান পাওয়া যাবে।\\$A$ সর্বনিম্ন হলে, $4\pi r-\frac{2}{r^2}=0$\\বা, $2\pi r^3=1$\\$\therefore r=\sqrt[3]{\frac{1}{2\pi}}=0.542$ dm $=5.42$ cm।\\এবং $h=2r=10.84$ cm।

**Final answer:** $r=5.42$ সেমি. এবং $h=10.84$ সেমি.

## ID 1343

**Question:** $y=\sqrt{x}$ গ্রাফে $(x,y)$ বিন্দুটির স্থানাঙ্ক নির্ণয় কর যা $(4,0)$ বিন্দুর নিকটতম।

**Solution:** দেওয়া আছে, $y=\sqrt{x}$\\$(x,y)$ বিন্দু হতে $(4,0)$ বিন্দুর দূরত্ব,\\$D=\sqrt{(4-x)^2+y^2}=\sqrt{(4-x)^2+x}$\\$\therefore \frac{dD}{dx}=\frac{2x-7}{2\sqrt{(4-x)^2+x}}$\\সর্বনিম্ন দূরত্বের জন্য, $\frac{dD}{dx}=0$\\বা, $2x-7=0$\\$\therefore x=\frac{7}{2}$\\$x=\frac{7}{2}$ হলে, $y=\sqrt{\frac{7}{2}}$।\\$\therefore$ নির্ণেয় বিন্দু $\left(\frac{7}{2},\sqrt{\frac{7}{2}}\right)$।

**Final answer:** নির্ণেয় বিন্দু $\left(\frac{7}{2},\sqrt{\frac{7}{2}}\right)$

## ID 1344

**Question:** $y=(x+1)(x-1)(x-3)$ বক্ররেখাটি যে সকল বিন্দুতে $x$-অক্ষকে ছেদ করে, ঐ সকল বিন্দুতে স্পর্শকের ঢাল নির্ণয় কর।

**Solution:** দেওয়া আছে, $y=(x+1)(x-1)(x-3)$।\\$x$-অক্ষকে ছেদ করলে $y=0$।\\$\therefore (x+1)(x-1)(x-3)=0$, তাই $x=-1,1,3$।\\ছেদবিন্দুগুলো $(-1,0),(1,0),(3,0)$।\\আবার, $y=x^3-3x^2-x+3$\\$\therefore \frac{dy}{dx}=3x^2-6x-1$।\\$x=-1,1,3$ হলে ঢাল যথাক্রমে $8,-4,8$।

**Final answer:** $8,-4,8$

## ID 1345

**Question:** $x^2+xy+y^2=4$ বক্ররেখার $(2,-2)$ বিন্দুতে স্পর্শকের ঢাল নির্ণয় কর।

**Solution:** দেওয়া আছে, $x^2+xy+y^2=4$।\\$x$ এর সাপেক্ষে অন্তরীকরণ করে,\\$2x+x\frac{dy}{dx}+y+2y\frac{dy}{dx}=0$\\$\therefore (x+2y)\frac{dy}{dx}=-(2x+y)$\\$\therefore \frac{dy}{dx}=-\frac{2x+y}{x+2y}$।\\$(2,-2)$ বিন্দুতে, $\frac{dy}{dx}=-\frac{4-2}{2-4}=1$।

**Final answer:** $1$

## ID 1346

**Question:** $y^2=4ax$ পরাবৃত্তের $(at^2,2at)$ বিন্দুতে স্পর্শকের ঢাল নির্ণয় কর।

**Solution:** দেওয়া আছে, $y^2=4ax$।\\$2y\frac{dy}{dx}=4a$\\$\therefore \frac{dy}{dx}=\frac{2a}{y}$।\\$(at^2,2at)$ বিন্দুতে, $\frac{dy}{dx}=\frac{2a}{2at}=\frac{1}{t}$।

**Final answer:** $\frac{1}{t}$

## ID 1347

**Question:** $y=x^3-x^2-7x+6$ বক্ররেখার যে সকল বিন্দুতে স্পর্শকের ঢাল শূন্য, তাদের স্থানাঙ্ক নির্ণয় কর।

**Solution:** দেওয়া আছে, $y=x^3-x^2-7x+6$।\\$\therefore \frac{dy}{dx}=3x^2-2x-7$।\\স্থিরবিন্দুর জন্য, $\frac{dy}{dx}=0$।\\$\therefore 3x^2-2x-7=0$ থেকে $x=2,-\frac{4}{3}$।\\$x=2$ হলে $y=-4$ এবং $x=-\frac{4}{3}$ হলে $y=\frac{302}{27}$।\\অতএব স্থিরবিন্দু $(2,-4),\left(-\frac{4}{3},\frac{302}{27}\right)$।

**Final answer:** $(2,-4),\left(-\frac{4}{3},\frac{302}{27}\right)$

## ID 1348

**Question:** $x^2-2y^2=10$ বক্ররেখার $(-4,3)$ বিন্দুতে স্পর্শকের ঢাল নির্ণয় কর।

**Solution:** দেওয়া আছে, $x^2-2y^2=10$।\\$2x-4y\frac{dy}{dx}=0$\\$\therefore \frac{dy}{dx}=\frac{x}{2y}$।\\$(-4,3)$ বিন্দুতে, $\frac{dy}{dx}=\frac{-4}{2\cdot3}=-\frac{2}{3}$।

**Final answer:** $-\frac{2}{3}$

## ID 1349

**Question:** নিম্নলিখিত বক্ররেখাসমূহের যে সকল বিন্দুতে স্পর্শক $x$-অক্ষের সমান্তরাল, তাদের স্থানাঙ্ক নির্ণয় কর: (i) $y=x^3-3x+2$

**Solution:** দেওয়া আছে, $y=x^3-3x+2$।\\$\therefore \frac{dy}{dx}=3x^2-3$।\\স্পর্শক $x$-অক্ষের সমান্তরাল হলে, $\frac{dy}{dx}=0$।\\$\therefore 3x^2-3=0$, অর্থাৎ $x=\pm1$।\\$x=1$ হলে $y=0$ এবং $x=-1$ হলে $y=4$।\\অতএব বিন্দুগুলো $(1,0),(-1,4)$।

**Final answer:** $(1,0),(-1,4)$

## ID 1350

**Question:** নিম্নলিখিত বক্ররেখাসমূহের যে সকল বিন্দুতে স্পর্শক $x$-অক্ষের সমান্তরাল, তাদের স্থানাঙ্ক নির্ণয় কর: (ii) $y=(x-3)^2(x-2)$

**Solution:** দেওয়া আছে, $y=(x-3)^2(x-2)$।\\$\therefore \frac{dy}{dx}=(x-3)^2+2(x-2)(x-3)$\\$=(x-3)(3x-7)$।\\স্পর্শক $x$-অক্ষের সমান্তরাল হলে, $\frac{dy}{dx}=0$।\\$\therefore x=3$ অথবা $x=\frac{7}{3}$।\\$x=3$ হলে $y=0$ এবং $x=\frac{7}{3}$ হলে $y=\frac{4}{27}$।\\অতএব বিন্দুগুলো $(3,0),\left(\frac{7}{3},\frac{4}{27}\right)$।

**Final answer:** $(3,0),\left(\frac{7}{3},\frac{4}{27}\right)$

## ID 1351

**Question:** নিম্নলিখিত বক্ররেখাসমূহের যে সকল বিন্দুতে স্পর্শক $x$-অক্ষের সমান্তরাল, তাদের স্থানাঙ্ক নির্ণয় কর: (iii) $x^2+y^2-2x-3=0$

**Solution:** দেওয়া আছে, $x^2+y^2-2x-3=0$।\\$2x+2y\frac{dy}{dx}-2=0$\\স্পর্শক $x$-অক্ষের সমান্তরাল হলে, $\frac{dy}{dx}=0$।\\$\therefore 2x-2=0$, অর্থাৎ $x=1$।\\সমীকরণে বসিয়ে, $1+y^2-2-3=0$ থেকে $y=\pm2$।\\অতএব বিন্দুগুলো $(1,2),(1,-2)$।

**Final answer:** $(1,2),(1,-2)$

## ID 1352

**Question:** নিম্নলিখিত বক্ররেখাসমূহের যে সকল বিন্দুতে স্পর্শক $x$-অক্ষের সমান্তরাল, তাদের স্থানাঙ্ক নির্ণয় কর: (iv) $y^3=x^2(2a-x)$

**Solution:** দেওয়া আছে, $y^3=x^2(2a-x)=2ax^2-x^3$।\\$3y^2\frac{dy}{dx}=4ax-3x^2$\\$\therefore \frac{dy}{dx}=\frac{4ax-3x^2}{3y^2}$।\\স্পর্শক $x$-অক্ষের সমান্তরাল হলে, $\frac{dy}{dx}=0$।\\$\therefore x(4a-3x)=0$, তাই $x=0$ অথবা $x=\frac{4a}{3}$।\\$x=0$ হলে $y=0$।\\$x=\frac{4a}{3}$ হলে $y^3=\frac{32a^3}{27}$, তাই $y=\frac{2a}{3}\sqrt[3]{4}$।\\অতএব বিন্দুগুলো $(0,0),\left(\frac{4a}{3},\frac{2a}{3}\sqrt[3]{4}\right)$।

**Final answer:** $(0,0),\left(\frac{4a}{3},\frac{2a}{3}\sqrt[3]{4}\right)$

## ID 1353

**Question:** নিম্নলিখিত বক্ররেখাসমূহের যে সকল বিন্দুতে স্পর্শক $x$-অক্ষের উপর লম্ব ($y$-অক্ষের সমান্তরাল) তা স্থানাঙ্ক নির্ণয় কর: (i) $y=x^2+\sqrt{1-x^2}$

**Solution:** দেওয়া আছে, $y=x^2+\sqrt{1-x^2}$।\\$\frac{dy}{dx}=2x-\frac{x}{\sqrt{1-x^2}}=\frac{2x\sqrt{1-x^2}-x}{\sqrt{1-x^2}}$।\\$\therefore \frac{dx}{dy}=\frac{\sqrt{1-x^2}}{2x\sqrt{1-x^2}-x}$।\\স্পর্শক $x$-অক্ষের উপর লম্ব হলে, $\frac{dx}{dy}=0$।\\$\therefore \sqrt{1-x^2}=0$, তাই $x=\pm1$।\\$x=1$ ও $x=-1$ উভয় ক্ষেত্রেই $y=1$।\\অতএব বিন্দুগুলো $(1,1),(-1,1)$।

**Final answer:** $(1,1),(-1,1)$

## ID 1354

**Question:** নিম্নলিখিত বক্ররেখাসমূহের যে সকল বিন্দুতে স্পর্শক $x$-অক্ষের উপর লম্ব ($y$-অক্ষের সমান্তরাল) তা স্থানাঙ্ক নির্ণয় কর: (ii) $x^2+4y^2=8$

**Solution:** দেওয়া আছে, $x^2+4y^2=8$।\\$2x+8y\frac{dy}{dx}=0$\\$\therefore \frac{dy}{dx}=-\frac{x}{4y}$ এবং $\frac{dx}{dy}=-\frac{4y}{x}$।\\স্পর্শক $x$-অক্ষের উপর লম্ব হলে, $\frac{dx}{dy}=0$।\\$\therefore y=0$।\\সমীকরণে বসিয়ে, $x^2=8$, তাই $x=\pm2\sqrt{2}$।\\অতএব বিন্দুগুলো $(-2\sqrt{2},0),(2\sqrt{2},0)$।

**Final answer:** $(-2\sqrt{2},0),(2\sqrt{2},0)$

## ID 1355

**Question:** নিম্নলিখিত বক্ররেখাসমূহের যে সকল বিন্দুতে স্পর্শক $x$-অক্ষের উপর লম্ব ($y$-অক্ষের সমান্তরাল) তা স্থানাঙ্ক নির্ণয় কর: (iii) $y^2=x^2(a-x)$

**Solution:** দেওয়া আছে, $y^2=x^2(a-x)=ax^2-x^3$।\\$2y\frac{dy}{dx}=2ax-3x^2$\\$\therefore \frac{dx}{dy}=\frac{2y}{2ax-3x^2}$।\\স্পর্শক $x$-অক্ষের উপর লম্ব হলে, $\frac{dx}{dy}=0$।\\$\therefore y=0$।\\সমীকরণে বসিয়ে, $0=x^2(a-x)$, তাই $x=0,a$।\\অতএব বিন্দুগুলো $(0,0),(a,0)$।

**Final answer:** $(0,0),(a,0)$

## ID 1356

**Question:** নিম্নলিখিত বক্ররেখাসমূহের যে সকল বিন্দুতে স্পর্শক $x$-অক্ষের উপর লম্ব ($y$-অক্ষের সমান্তরাল) তা স্থানাঙ্ক নির্ণয় কর: (iv) $x^2+4x+y^2=0$

**Solution:** দেওয়া আছে, $x^2+4x+y^2=0$।\\$2x+4+2y\frac{dy}{dx}=0$\\$\therefore \frac{dx}{dy}=\frac{-y}{x+2}$।\\স্পর্শক $x$-অক্ষের উপর লম্ব হলে, $\frac{dx}{dy}=0$।\\$\therefore y=0$।\\সমীকরণে বসিয়ে, $x^2+4x=0$, তাই $x=0,-4$।\\অতএব বিন্দুগুলো $(0,0),(-4,0)$।

**Final answer:** $(0,0),(-4,0)$

## ID 1357

**Question:** $y=x^3-3x^2-2x+1$ বক্ররেখার যে সকল বিন্দুতে স্পর্শকগুলি অক্ষদ্বয়ের সাথে সমান সমান কোণ উৎপন্ন করে, তাদের ভুজ নির্ণয় কর।

**Solution:** দেওয়া আছে, $y=x^3-3x^2-2x+1$।\\$\therefore \frac{dy}{dx}=3x^2-6x-2$।\\স্পর্শক অক্ষদ্বয়ের সাথে সমান কোণ উৎপন্ন করলে, $\frac{dy}{dx}=\pm1$।\\$\frac{dy}{dx}=1$ হলে, $3x^2-6x-3=0$, তাই $x=1\pm\sqrt{2}$।\\$\frac{dy}{dx}=-1$ হলে, $3x^2-6x-1=0$, তাই $x=1\pm\frac{2}{\sqrt{3}}$।

**Final answer:** $1\pm\sqrt{2},\ 1\pm\frac{2}{\sqrt{3}}$

## ID 1358

**Question:** $a$-এর মান কত হলে, $y=ax(1-x)$ বক্ররেখার মূলবিন্দুতে স্পর্শকটি $x$-অক্ষের সাথে $60^\circ$ কোণ উৎপন্ন করবে।

**Solution:** দেওয়া আছে, $y=ax(1-x)=ax-ax^2$।\\$\therefore \frac{dy}{dx}=a-2ax$।\\মূলবিন্দুতে স্পর্শকের ঢাল $=a$।\\প্রশ্নমতে, $a=\tan60^\circ=\sqrt{3}$।

**Final answer:** $a=\sqrt{3}$

## ID 1359

**Question:** $b$ এর মান কত হলে $y=bx(x-1)$ বক্ররেখার মূলবিন্দুতে স্পর্শকটি $x$ অক্ষের ধনাত্মক দিকের সাথে $45^\circ$ কোণ উৎপন্ন করবে।

**Solution:** দেওয়া আছে, $y=bx(x-1)$।\\$\therefore y=bx^2-bx$\\$\therefore \frac{dy}{dx}=2bx-b$।\\মূলবিন্দুতে, $\frac{dy}{dx}=-b$।\\স্পর্শক মূলবিন্দুতে $45^\circ$ কোণ উৎপন্ন করলে, $-b=\tan45^\circ=1$।\\$\therefore b=-1$।

**Final answer:** $b=-1$

## ID 1360

**Question:** নিম্নলিখিত বক্ররেখাসমূহের উল্লিখিত বিন্দুতে স্পর্শক ও অভিলম্বের সমীকরণ নির্ণয় কর: (i) $y=x^3-2x^2+4$ বক্ররেখার $(2,4)$ বিন্দুতে।

**Solution:** দেওয়া আছে, $y=x^3-2x^2+4$।\\$\therefore \frac{dy}{dx}=3x^2-4x$।\\$(2,4)$ বিন্দুতে ঢাল $=12-8=4$।\\স্পর্শকের সমীকরণ, $y-4=4(x-2)$\\$\therefore 4x-y-4=0$।\\অভিলম্বের সমীকরণ, $(x-2)+4(y-4)=0$\\$\therefore x+4y-18=0$।

**Final answer:** Tangent: $4x-y-4=0$; normal: $x+4y-18=0$

## ID 1361

**Question:** নিম্নলিখিত বক্ররেখাসমূহের উল্লিখিত বিন্দুতে স্পর্শক ও অভিলম্বের সমীকরণ নির্ণয় কর: (ii) $y=x^3-3x+2$ বক্ররেখার $(2,-2)$ বিন্দুতে।

**Solution:** দেওয়া আছে, $y=x^3-3x+2$।\\$\therefore \frac{dy}{dx}=3x^2-3$।\\$(2,-2)$ বিন্দুতে ঢাল $=3(2)^2-3=9$।\\স্পর্শকের সমীকরণ, $y+2=9(x-2)$\\$\therefore 9x-y-20=0$।\\অভিলম্বের সমীকরণ, $(x-2)+9(y+2)=0$\\$\therefore x+9y+16=0$।

**Final answer:** Tangent: $9x-y-20=0$; normal: $x+9y+16=0$

## ID 1362

**Question:** নিম্নলিখিত বক্ররেখাসমূহের উল্লিখিত বিন্দুতে স্পর্শক ও অভিলম্বের সমীকরণ নির্ণয় কর: (iii) $x^2-y^2=7$ বক্ররেখার $(-4,3)$ বিন্দুতে।

**Solution:** দেওয়া আছে, $x^2-y^2=7$।\\$2x-2y\frac{dy}{dx}=0$\\$\therefore \frac{dy}{dx}=\frac{x}{y}$।\\$(-4,3)$ বিন্দুতে স্পর্শকের ঢাল $=-\frac{4}{3}$।\\স্পর্শকের সমীকরণ, $y-3=-\frac{4}{3}(x+4)$\\$\therefore 4x+3y+7=0$।\\অভিলম্বের সমীকরণ, $(x+4)+\frac{4}{3}(y-3)=0$\\$\therefore 3x-4y+24=0$।

**Final answer:** Tangent: $4x+3y+7=0$; normal: $3x-4y+24=0$

## ID 1363

**Question:** নিম্নলিখিত বক্ররেখাসমূহের উল্লিখিত বিন্দুতে স্পর্শক ও অভিলম্বের সমীকরণ নির্ণয় কর: (iv) $x^2-y^2=7$ বক্ররেখার $(4,-3)$ বিন্দুতে।

**Solution:** দেওয়া আছে, $x^2-y^2=7$।\\$2x-2y\frac{dy}{dx}=0$\\$\therefore \frac{dy}{dx}=\frac{x}{y}$।\\$(4,-3)$ বিন্দুতে স্পর্শকের ঢাল $=-\frac{4}{3}$।\\স্পর্শকের সমীকরণ, $y+3=-\frac{4}{3}(x-4)$\\$\therefore 4x+3y-7=0$।\\অভিলম্বের সমীকরণ, $(x-4)+\frac{4}{3}(y+3)=0$\\$\therefore 3x-4y-24=0$।

**Final answer:** Tangent: $4x+3y-7=0$; normal: $3x-4y-24=0$

## ID 1364

**Question:** নিম্নলিখিত বক্ররেখাসমূহের উল্লিখিত বিন্দুতে স্পর্শক ও অভিলম্বের সমীকরণ নির্ণয় কর: (v) $x^2+y^2-6x-10y+21=0$ বৃত্তের $(1,2)$ বিন্দুতে।

**Solution:** (v) দেওয়া আছে, $x^2+y^2-6x-10y+21=0$\\$2x+2y\frac{dy}{dx}-6-10\frac{dy}{dx}=0$\\বা, $x+y\frac{dy}{dx}-3-5\frac{dy}{dx}=0$\\বা, $\frac{dy}{dx}(y-5)=3-x$\\$\therefore \frac{dy}{dx}=\frac{3-x}{y-5}$\\এখন $(1,2)$ বিন্দুতে, $\frac{dy}{dx}=\frac{3-1}{2-5}=-\frac{2}{3}$\\$\therefore$ স্পর্শকের সমীকরণ, $y-2=-\frac{2}{3}(x-1)$\\বা, $2x+3y-8=0$।\\এবং অভিলম্বের সমীকরণ, $(x-1)-\frac{2}{3}(y-2)=0$\\বা, $3x-2y+1=0$।

**Final answer:** স্পর্শক: $2x+3y-8=0$; অভিলম্ব: $3x-2y+1=0$

## ID 1365

**Question:** নিম্নলিখিত বক্ররেখাসমূহের উল্লিখিত বিন্দুতে স্পর্শক ও অভিলম্বের সমীকরণ নির্ণয় কর: (vi) $x^2+y^2+6x-3y-5=0$ বৃত্তের $(1,2)$ বিন্দুতে।

**Solution:** (vi) দেওয়া আছে, $x^2+y^2+6x-3y-5=0$\\$x$ এর সাপেক্ষে অন্তরীকরণ করে পাই,\\$2x+2y\frac{dy}{dx}+6-3\frac{dy}{dx}=0$\\বা, $\frac{dy}{dx}(2y-3)=-(6+2x)$\\$\therefore \frac{dy}{dx}=\frac{-(6+2x)}{2y-3}$\\এখন, $(1,2)$ বিন্দুতে, $\frac{dy}{dx}=\frac{-(6+2\cdot1)}{2\cdot2-3}=-8$\\$\therefore$ স্পর্শকের সমীকরণ, $y-2=-8(x-1)$\\বা, $8x+y-10=0$।\\এবং অভিলম্বের সমীকরণ, $(x-1)-8(y-2)=0$\\বা, $x-8y+15=0$।

**Final answer:** স্পর্শক: $8x+y-10=0$; অভিলম্ব: $x-8y+15=0$

## ID 1366

**Question:** নিম্নলিখিত বক্ররেখাসমূহের উল্লিখিত বিন্দুতে স্পর্শক ও অভিলম্বের সমীকরণ নির্ণয় কর: (vii) $y(x-2)(x-3)-x+7=0$ বক্ররেখাটি $x$ অক্ষকে যে বিন্দুতে ছেদ করে ঐ বিন্দুতে।

**Solution:** (vii) দেওয়া আছে, $y(x-2)(x-3)-x+7=0$\\$x$ অক্ষকে ছেদ করলে ছেদবিন্দুর $y$ এর স্থানাঙ্ক $0$।\\তাই, $0-x+7=0$ বা, $x=7$\\অতএব, ছেদবিন্দুর স্থানাঙ্ক $(7,0)$।\\$x$ এর সাপেক্ষে অন্তরীকরণ করে পাই,\\$\frac{dy}{dx}(x-2)(x-3)+y(x-2)+y(x-3)-1=0$\\বা, $\frac{dy}{dx}=\frac{-y(x-2)-y(x-3)+1}{(x-2)(x-3)}$\\$(7,0)$ বিন্দুতে, $\frac{dy}{dx}=\frac{1}{(7-2)(7-3)}=\frac{1}{20}$\\$\therefore$ স্পর্শকের সমীকরণ, $y-0=\frac{1}{20}(x-7)$\\বা, $x-20y=7$।\\এবং অভিলম্বের সমীকরণ, $\frac{1}{20}(y-0)+(x-7)=0$\\বা, $20x+y=140$।

**Final answer:** স্পর্শক: $x-20y=7$; অভিলম্ব: $20x+y=140$

## ID 1367

**Question:** নিম্নলিখিত বক্ররেখাসমূহের উল্লিখিত বিন্দুতে স্পর্শক ও অভিলম্বের সমীকরণ নির্ণয় কর: (viii) $y(x-1)(x-2)-x+3=0$ বক্ররেখাটি যে বিন্দুতে $x$ অক্ষকে ছেদ করে উক্ত বিন্দুতে।

**Solution:** (viii) দেওয়া আছে, $y(x-1)(x-2)-x+3=0$\\$x$ অক্ষকে ছেদ করলে ছেদবিন্দুর $y$ স্থানাঙ্ক $0$।\\অর্থাৎ $0-x+3=0$, তাই $x=3$\\অতএব, ছেদবিন্দুর স্থানাঙ্ক $(3,0)$।\\$y(x^2-3x+2)-x+3=0$\\$\therefore y(2x-3)+(x^2-3x+2)\frac{dy}{dx}-1=0$\\বা, $\frac{dy}{dx}=\frac{1-y(2x-3)}{x^2-3x+2}$\\$(3,0)$ বিন্দুতে, $\frac{dy}{dx}=\frac{1}{2}$\\$\therefore$ স্পর্শকের সমীকরণ, $y-0=\frac{1}{2}(x-3)$\\বা, $x-2y-3=0$।\\অভিলম্বের সমীকরণ, $(x-3)+\frac{1}{2}(y-0)=0$\\বা, $2x+y-6=0$।

**Final answer:** স্পর্শক: $x-2y-3=0$; অভিলম্ব: $2x+y-6=0$

## ID 1368

**Question:** নিম্নলিখিত বক্ররেখাসমূহের উল্লিখিত বিন্দুতে স্পর্শক ও অভিলম্বের সমীকরণ নির্ণয় কর: (ix) $x^2+y^2-10x-8y+16=0$ বক্ররেখাটির $(10,4)$ বিন্দুতে।

**Solution:** (ix) প্রদত্ত বক্ররেখার সমীকরণ, $x^2+y^2-10x-8y+16=0$\\$x$ এর সাপেক্ষে অন্তরীকরণ করে পাই,\\$2x+2y\frac{dy}{dx}-10-8\frac{dy}{dx}=0$\\বা, $(2y-8)\frac{dy}{dx}=10-2x$\\$\therefore \frac{dy}{dx}=\frac{10-2x}{2y-8}$\\$(10,4)$ বিন্দুতে $\frac{dy}{dx}=\frac{10-20}{8-8}=\frac{1}{0}{0}$\\$\therefore$ স্পর্শকের সমীকরণ, $y-4=\frac{1}{0}{0}(x-10)$\\বা, $x-10=0$।\\এবং অভিলম্বের সমীকরণ, $y-4=-\frac{0}{10}(x-10)$\\বা, $y-4=0$।

**Final answer:** স্পর্শক: $x-10=0$; অভিলম্ব: $y-4=0$

## ID 1369

**Question:** নিম্নলিখিত বক্ররেখাসমূহের উল্লিখিত বিন্দুতে স্পর্শক ও অভিলম্বের সমীকরণ নির্ণয় কর: (x) $x^2-2y^2-7=0$ বক্ররেখার $(3,1)$ বিন্দুতে।

**Solution:** (x) দেওয়া আছে, $g(x,y)=x^2-2y^2-7$\\প্রশ্নমতে, $g(x,y)=0$ বা, $x^2-2y^2-7=0$\\$x$ এর সাপেক্ষে অন্তরীকরণ করে, $2x-4y\frac{dy}{dx}=0$\\বা, $4y\frac{dy}{dx}=2x$\\$\therefore \frac{dy}{dx}=\frac{x}{2y}$\\$(3,1)$ বিন্দুতে স্পর্শকের ঢাল $=\frac{3}{2\cdot1}=\frac{3}{2}$।\\$\therefore$ স্পর্শকের সমীকরণ, $y-1=\frac{3}{2}(x-3)$\\বা, $3x-2y-7=0$।\\এবং অভিলম্বের সমীকরণ, $x-3+\frac{3}{2}(y-1)=0$\\বা, $2x+3y-9=0$।

**Final answer:** স্পর্শক: $3x-2y-7=0$; অভিলম্ব: $2x+3y-9=0$

## ID 1370

**Question:** নিম্নলিখিত বক্ররেখাসমূহের উল্লিখিত বিন্দুতে স্পর্শক ও অভিলম্বের সমীকরণ নির্ণয় কর: (xi) $y(x+1)(x+2)-x+4=0$ বক্ররেখাটি যে বিন্দুতে $x$ অক্ষকে ছেদ করে।

**Solution:** (xi) দেওয়া আছে, $y(x+1)(x+2)-x+4=0$\\যেহেতু বক্ররেখাটি $x$-অক্ষকে ছেদ করে, সেহেতু $y=0$।\\অতএব, $0(x+1)(x+2)-x+4=0$ বা, $x=4$।\\ছেদবিন্দু $(4,0)$।\\$y(x^2+3x+2)-x+4=0$\\$x$ এর সাপেক্ষে অন্তরীকরণ করে,\\$y(2x+3)+(x^2+3x+2)\frac{dy}{dx}-1=0$\\বা, $\frac{dy}{dx}=\frac{1-2xy-3y}{x^2+3x+2}$\\$(4,0)$ বিন্দুতে, $\frac{dy}{dx}=\frac{1}{30}$।\\$\therefore$ স্পর্শকের সমীকরণ, $y-0=\frac{1}{30}(x-4)$\\বা, $x-30y-4=0$।\\$(4,0)$ বিন্দুতে অভিলম্বের সমীকরণ, $(x-4)+\frac{1}{30}(y-0)=0$\\বা, $30x+y=120$।

**Final answer:** স্পর্শক: $x-30y-4=0$; অভিলম্ব: $30x+y=120$

## ID 1371

**Question:** নিম্নলিখিত বক্ররেখাসমূহের উল্লিখিত বিন্দুতে স্পর্শক ও অভিলম্বের সমীকরণ নির্ণয় কর: (xii) $y^2-4x-6y+20=0$ বক্ররেখার $(3,2)$ বিন্দুতে।

**Solution:** (xii) দেওয়া আছে, $y^2-4x-6y+20=0$\\বা, $2y\frac{dy}{dx}-4-6\frac{dy}{dx}=0$\\বা, $(2y-6)\frac{dy}{dx}=4$\\$\therefore \frac{dy}{dx}=\frac{4}{2y-6}$\\$\therefore \left(\frac{dy}{dx}\right)_{(3,2)}=\frac{4}{2\cdot2-6}=-2$\\$(3,2)$ বিন্দুতে স্পর্শকের ঢাল $=-2$ এবং অভিলম্বের ঢাল $=\frac{1}{2}$।\\স্পর্শকের সমীকরণ, $y-2=-2(x-3)$\\বা, $2x+y-8=0$।\\অভিলম্বের সমীকরণ, $y-2=\frac{1}{2}(x-3)$\\বা, $x-2y+1=0$।

**Final answer:** স্পর্শক: $2x+y-8=0$; অভিলম্ব: $x-2y+1=0$

## ID 1372

**Question:** নিম্নলিখিত বক্ররেখাসমূহের উল্লিখিত বিন্দুতে স্পর্শক ও অভিলম্বের সমীকরণ নির্ণয় কর: (xiii) $y=3x^2+2x+7$ বক্ররেখার $(2,23)$ বিন্দুতে।

**Solution:** (xiii) দেওয়া আছে, $y=3x^2+2x+7$\\$\therefore \frac{dy}{dx}=6x+2$\\এখন, $(2,23)$ বিন্দুতে, $\frac{dy}{dx}=6\cdot2+2=14$\\$\therefore$ $(2,23)$ বিন্দুতে স্পর্শকের ঢাল $=14$ এবং অভিলম্বের ঢাল $=-\frac{1}{14}$।\\$\therefore$ স্পর্শকের সমীকরণ, $y-23=14(x-2)$\\বা, $14x-y-5=0$।\\এবং অভিলম্বের সমীকরণ, $y-23=-\frac{1}{14}(x-2)$\\বা, $x+14y-324=0$।

**Final answer:** স্পর্শক: $14x-y-5=0$; অভিলম্ব: $x+14y-324=0$

## ID 1373

**Question:** $y^2=4ax$ পরাবৃত্তের $(x_1,y_1)$ বিন্দুতে স্পর্শকের সমীকরণ নির্ণয় কর।

**Solution:** (i) দেওয়া আছে, $y^2=4ax$\\বা, $2y\frac{dy}{dx}=4a$\\$\therefore \frac{dy}{dx}=\frac{2a}{y}$\\এখন, $(x_1,y_1)$ বিন্দুতে, $\frac{dy}{dx}=\frac{2a}{y_1}$।\\অতএব, পরাবৃত্তের $(x_1,y_1)$ বিন্দুতে স্পর্শকের সমীকরণ,\\$y-y_1=\frac{2a}{y_1}(x-x_1)$\\বা, $yy_1-y_1^2=2ax-2ax_1$\\বা, $yy_1=2ax+y_1^2-2ax_1$\\বা, $yy_1=2ax+2ax_1=2a(x+x_1)$।

**Final answer:** স্পর্শকের সমীকরণ $yy_1=2a(x+x_1)$

## ID 1374

**Question:** $x^3-3axy+y^3=0$ বক্ররেখার $(x_1,y_1)$ বিন্দুতে অভিলম্বের সমীকরণ নির্ণয় কর।

**Solution:** (ii) দেওয়া আছে, $x^3-3axy+y^3=0$\\বা, $3x^2-3ay-3ax\frac{dy}{dx}+3y^2\frac{dy}{dx}=0$\\বা, $x^2-ay-(ax-y^2)\frac{dy}{dx}=0$\\$\therefore \frac{dy}{dx}=\frac{x^2-ay}{ax-y^2}$\\$\therefore (x_1,y_1)$ বিন্দুতে অভিলম্বের সমীকরণ,\\$(x_1-x)+\frac{x_1^2-ay_1}{ax_1-y_1^2}(y-y_1)=0$\\বা, $(x-x_1)(ax_1-y_1^2)+(x_1^2-ay_1)(y-y_1)=0$\\$\therefore (y-y_1)(x_1^2-ay_1)=(x-x_1)(y_1^2-ax_1)$।

**Final answer:** অভিলম্বের সমীকরণ $(y-y_1)(x_1^2-ay_1)=(x-x_1)(y_1^2-ax_1)$

## ID 1375

**Question:** $x^3-3xy+y^3=3$ বক্ররেখাটির $(1,-1)$ বিন্দু দিয়ে অতিক্রমকারী স্পর্শকের সমীকরণ নির্ণয় কর।

**Solution:** (iii) দেওয়া আছে, $x^3-3xy+y^3=3$\\বা, $\frac{d}{dx}(x^3)-3\frac{d}{dx}(xy)+\frac{d}{dx}(y^3)=\frac{d}{dx}(3)$\\বা, $3x^2-3\left[x\frac{dy}{dx}+y\cdot1\right]+3y^2\frac{dy}{dx}=0$\\বা, $x^2-y-x\frac{dy}{dx}+y^2\frac{dy}{dx}=0$\\বা, $(y^2-x)\frac{dy}{dx}=y-x^2$\\$\therefore \frac{dy}{dx}=\frac{y-x^2}{y^2-x}$\\$(1,-1)$ বিন্দুতে, $\frac{dy}{dx}=\frac{-1-1}{(-1)^2-1}=\frac{-2}{0}$\\এখন, $(1,-1)$ বিন্দুতে স্পর্শকের সমীকরণ,\\$y+1=\frac{-2}{0}(x-1)$\\$\therefore x-1=0$।

**Final answer:** স্পর্শকের সমীকরণ $x-1=0$

## ID 1376

**Question:** $y=x^3-2x^2+2$ বক্ররেখার $(2,2)$ বিন্দুতে স্পর্শকের সমীকরণ নির্ণয় কর।

**Solution:** (iv) $y=x^3-2x^2+2$\\$\therefore \frac{dy}{dx}=3x^2-4x$\\$(2,2)$ বিন্দুতে, $\frac{dy}{dx}=3\cdot2^2-4(2)=12-8=4$\\$\therefore$ প্রদত্ত বক্ররেখার $(2,2)$ বিন্দুতে স্পর্শকের সমীকরণ,\\$y-2=4(x-2)$\\বা, $4x-y-6=0$।

**Final answer:** স্পর্শকের সমীকরণ $4x-y-6=0$

## ID 1377

**Question:** $x^2-5xy+y^2-5x+6y+9=0$ বক্ররেখার $(2,1)$ বিন্দুতে অভিলম্বের সমীকরণ নির্ণয় কর।

**Solution:** (v) $x^2-5xy+y^2-5x+6y+9=0$\\$x$-এর সাপেক্ষে অন্তরীকরণ করে পাই,\\$2x-5x\frac{dy}{dx}-5y+2y\frac{dy}{dx}-5+6\frac{dy}{dx}=0$\\বা, $(5x-2y-6)\frac{dy}{dx}=2x-5y-5$\\$\therefore \frac{dy}{dx}=\frac{2x-5y-5}{5x-2y-6}$\\$(2,1)$ বিন্দুতে $\frac{dy}{dx}=\frac{4-5-5}{10-2-6}=\frac{-6}{2}=-3$\\$(2,1)$ বিন্দুতে বক্ররেখার অভিলম্বের সমীকরণ,\\$y-1=\frac{1}{3}(x-2)$\\বা, $x-3y+1=0$।

**Final answer:** অভিলম্বের সমীকরণ $x-3y+1=0$

## ID 1378

**Question:** $(-3,2)$ বিন্দুতে $x^2-y^2=5$ বক্ররেখার স্পর্শকের সমীকরণ নির্ণয় কর।

**Solution:** (vi) $(-3,2)$ বিন্দুতে $x^2-y^2=5$ বক্ররেখার স্পর্শকের সমীকরণ,\\$x_1x-y_1y=5$\\বা, $-3x-2y=5$\\$\therefore 3x+2y+5=0$।

**Final answer:** স্পর্শকের সমীকরণ $3x+2y+5=0$

## ID 1379

**Question:** $f(x)=\frac{\ln x}{x^2+1}$ বক্ররেখার $x=2$ বিন্দুতে স্পর্শকের সমীকরণ নির্ণয় কর।

**Solution:** (vii) দেওয়া আছে, $y=f(x)=\frac{\ln x}{x^2+1}$\\এখন, $x=2$ হলে, $y=\frac{\ln2}{2^2+1}=\frac{\ln2}{5}$।\\$\frac{dy}{dx}=\frac{(x^2+1)\frac{1}{x}-\ln x(2x)}{(x^2+1)^2}$\\$x=2$ বিন্দুতে $\frac{dy}{dx}=\frac{4+1-2\cdot2\cdot2\ln2}{2\cdot25}=\frac{5-8\ln2}{50}$\\$\therefore x=2$ বিন্দুতে স্পর্শকের সমীকরণ,\\$y-\frac{\ln2}{5}=\frac{5-8\ln2}{50}(x-2)$।

**Final answer:** স্পর্শকের সমীকরণ $y-\frac{\ln2}{5}=\frac{5-8\ln2}{50}(x-2)$

## ID 1380

**Question:** দেখাও যে, $\sqrt{x}+\sqrt{y}=\sqrt{a}$ বক্ররেখার যে কোনো বিন্দুতে অঙ্কিত স্পর্শক কর্তৃক অক্ষদ্বয় হতে কর্তিত অংশদ্বয়ের যোগফল ধ্রুবক।

**Solution:** (viii) $\sqrt{x}+\sqrt{y}=\sqrt{a}$\\বা, $\frac{1}{2\sqrt{x}}+\frac{1}{2\sqrt{y}}\frac{dy}{dx}=0$\\বা, $\frac{dy}{dx}=-\frac{\sqrt{y}}{\sqrt{x}}$\\ধরি, স্পর্শবিন্দু $(x_1,y_1)$।\\$\therefore (x_1,y_1)$ বিন্দুতে ঢাল $=-\frac{\sqrt{y_1}}{\sqrt{x_1}}$।\\এবং বক্ররেখাটি $(x_1,y_1)$ বিন্দুগামী হওয়ায়, $\sqrt{x_1}+\sqrt{y_1}=\sqrt{a}$।\\$\therefore$ স্পর্শকের সমীকরণ, $y-y_1=-\frac{\sqrt{y_1}}{\sqrt{x_1}}(x-x_1)$\\বা, $\sqrt{x_1}y+\sqrt{y_1}x=\sqrt{x_1}y_1+\sqrt{y_1}x_1$\\বা, $\frac{x}{\sqrt{x_1}}+\frac{y}{\sqrt{y_1}}=\sqrt{y_1}+\sqrt{x_1}$\\বা, $\frac{x}{\sqrt{a}\sqrt{x_1}}+\frac{y}{\sqrt{a}\sqrt{y_1}}=1$\\$\therefore x$ এবং $y$ অক্ষ বরাবর কর্তিত অংশের পরিমাণ যথাক্রমে $\sqrt{a}\sqrt{x_1}$ এবং $\sqrt{a}\sqrt{y_1}$।\\কর্তিত অংশ দুইটির যোগফল $=\sqrt{a}\sqrt{x_1}+\sqrt{a}\sqrt{y_1}$\\$=\sqrt{a}(\sqrt{x_1}+\sqrt{y_1})=\sqrt{a}\sqrt{a}=a$, যা একটি ধ্রুবক।

**Final answer:** কর্তিত অংশদ্বয়ের যোগফল $=a$, যা ধ্রুবক

## ID 1381

**Question:** নিম্নলিখিত ফাংশনগুলির সর্বনিম্ন মান ও সর্বোচ্চ মান (লঘিষ্ঠ মান ও গরিষ্ঠ মান) নির্ণয় কর: (i) $x^3-3x^2-45x+13$

**Solution:** (i) ধরি, $y=x^3-3x^2-45x+13$\\$\therefore \frac{dy}{dx}=3x^2-6x-45$ এবং $\frac{d^2y}{dx^2}=6x-6$\\সর্বনিম্ন ও সর্বোচ্চ মানের জন্য, $\frac{dy}{dx}=0$\\বা, $3x^2-6x-45=0$\\বা, $x^2-2x-15=0$\\বা, $(x-5)(x+3)=0$; $\therefore x=5$ অথবা $-3$\\যখন $x=5$, $\frac{d^2y}{dx^2}=6\cdot5-6=24>0$\\$\therefore x=5$ তে ফাংশনটির সর্বনিম্ন মান বিদ্যমান।\\$\therefore$ সর্বনিম্ন মান $=(5)^3-3(5)^2-45\cdot5+13=-162$।\\যখন $x=-3$, $\frac{d^2y}{dx^2}=6(-3)-6=-24<0$\\$\therefore x=-3$ তে ফাংশনটির সর্বোচ্চ মান বিদ্যমান।\\$\therefore$ সর্বোচ্চ মান $=(-3)^3-3(-3)^2-45(-3)+13=94$।

**Final answer:** সর্বনিম্ন মান $=-162$, সর্বোচ্চ মান $=94$

## ID 1382

**Question:** নিম্নলিখিত ফাংশনগুলির সর্বনিম্ন মান ও সর্বোচ্চ মান (লঘিষ্ঠ মান ও গরিষ্ঠ মান) নির্ণয় কর: (ii) $x^4-8x^3+22x^2-24x+5$

**Solution:** (ii) ধরি, $f(x)=x^4-8x^3+22x^2-24x+5$\\$\therefore f'(x)=4x^3-24x^2+44x-24$\\সর্বনিম্ন ও সর্বোচ্চ মানের জন্য, $f'(x)=0$\\বা, $4x^3-24x^2+44x-24=0$\\বা, $x^3-6x^2+11x-6=0$\\বা, $(x-1)(x-2)(x-3)=0$\\$\therefore x=1,2,3$\\$f''(x)=12x^2-48x+44$\\$x=1$ বিন্দুতে, $f''(x)=8>0$, তাই সর্বনিম্ন মান $=1-8+22-24+5=-4$।\\$x=2$ বিন্দুতে, $f''(x)=-4<0$, তাই সর্বোচ্চ মান $=16-64+88-48+5=-3$।\\$x=3$ বিন্দুতে, $f''(x)=8>0$, তাই সর্বনিম্ন মান $=81-216+198-72+5=-4$।

**Final answer:** সর্বনিম্ন মান $=-4$, সর্বোচ্চ মান $=-3$

## ID 1383

**Question:** নিম্নলিখিত ফাংশনগুলির সর্বনিম্ন মান ও সর্বোচ্চ মান (লঘিষ্ঠ মান ও গরিষ্ঠ মান) নির্ণয় কর: (iii) $x^3-6x^2+9x+5$

**Solution:** (iii) ধরি, $f(x)=x^3-6x^2+9x+5$\\$\therefore f'(x)=3x^2-12x+9$\\সর্বনিম্ন ও সর্বোচ্চ মানের জন্য, $f'(x)=0$\\বা, $3x^2-12x+9=0$\\বা, $x^2-4x+3=0$\\বা, $(x-1)(x-3)=0$\\$\therefore x=1,3$\\আবার, $f''(x)=6x-12$\\$x=3$ হলে, $f''(x)=6>0$, তাই ফাংশনটির সর্বনিম্ন মান বিদ্যমান।\\$\therefore$ সর্বনিম্ন মান $=(3)^3-6(3)^2+9\cdot3+5=5$।\\$x=1$ হলে, $f''(x)=-6<0$, তাই ফাংশনটির সর্বোচ্চ মান বিদ্যমান।\\$\therefore$ সর্বোচ্চ মান $=(1)^3-6(1)^2+9\cdot1+5=9$।

**Final answer:** সর্বোচ্চ মান $=9$, সর্বনিম্ন মান $=5$

## ID 1384

**Question:** নিম্নলিখিত ফাংশনগুলির সর্বনিম্ন মান ও সর্বোচ্চ মান (লঘিষ্ঠ মান ও গরিষ্ঠ মান) নির্ণয় কর: (iv) $x(12-2x)^2$

**Solution:** (iv) মনে করি, $y=x(12-2x)^2=4x(6-x)^2$\\বা, $y=144x-48x^2+4x^3$\\$\therefore \frac{dy}{dx}=144-96x+12x^2$\\সর্বোচ্চ ও সর্বনিম্ন মানের জন্য, $\frac{dy}{dx}=0$\\বা, $12x^2-96x+144=0$\\বা, $x^2-8x+12=0$\\বা, $(x-6)(x-2)=0$\\$\therefore x=6,2$\\আবার, $\frac{d^2y}{dx^2}=-96+24x$\\$x=6$ হলে, $\frac{d^2y}{dx^2}=48>0$, তাই $x=6$ বিন্দুতে সর্বনিম্ন মান বিদ্যমান এবং মান $6(12-12)^2=0$।\\$x=2$ হলে, $\frac{d^2y}{dx^2}=-48<0$, তাই $x=2$ বিন্দুতে সর্বোচ্চ মান বিদ্যমান এবং মান $2(12-4)^2=128$।

**Final answer:** সর্বনিম্ন মান $=0$, সর্বোচ্চ মান $=128$

## ID 1385

**Question:** নিম্নলিখিত ফাংশনগুলির সর্বনিম্ন মান ও সর্বোচ্চ মান (লঘিষ্ঠ মান ও গরিষ্ঠ মান) নির্ণয় কর: (v) $4x^3+3x^2-6x+30$

**Solution:** (v) ধরি, $g(x)=4x^3+3x^2-6x+30$\\$g'(x)=12x^2+6x-6=0$\\বা, $2x^2+x-1=0$\\বা, $(2x-1)(x+1)=0$\\$\therefore x=-1,\frac{1}{2}$\\এখন, $g''(x)=24x+6$\\$g''\left(\frac{1}{2}\right)=18>0$, তাই $x=\frac{1}{2}$ এর জন্য ফাংশনটির লঘুমান বিদ্যমান।\\লঘুমান $=g\left(\frac{1}{2}\right)=4\left(\frac{1}{2}\right)^3+3\left(\frac{1}{2}\right)^2-6\left(\frac{1}{2}\right)+30=\frac{113}{4}$।\\এবং $g''(-1)=-18<0$, তাই $x=-1$ এর জন্য ফাংশনটির গরিষ্ঠমান বিদ্যমান।\\গরিষ্ঠমান $=g(-1)=4(-1)^3+3(-1)^2-6(-1)+30=35$।

**Final answer:** লঘুমান $=\frac{113}{4}$, গরিষ্ঠমান $=35$

## ID 1386

**Question:** নিম্নলিখিত ফাংশনগুলির সর্বনিম্ন মান ও সর্বোচ্চ মান (লঘিষ্ঠ মান ও গরিষ্ঠ মান) নির্ণয় কর: (vi) $\frac{1}{3}x^3+\frac{1}{2}x^2-6x+8$

**Solution:** (vi) ধরি, $f(x)=\frac{1}{3}x^3+\frac{1}{2}x^2-6x+8$\\$f'(x)=x^2+x-6$\\সর্বনিম্ন ও সর্বোচ্চ মানের জন্য, $f'(x)=0$\\বা, $x^2+x-6=0$\\বা, $(x+3)(x-2)=0$\\$\therefore x=-3,2$\\আবার, $f''(x)=2x+1$\\$x=-3$ বিন্দুতে, $f''(x)=-5<0$, তাই ফাংশনটির গরিষ্ঠমান বিদ্যমান।\\$\therefore$ সর্বোচ্চ মান $=\frac{1}{3}(-3)^3+\frac{1}{2}(-3)^2-6(-3)+8=\frac{43}{2}$।\\$x=2$ বিন্দুতে, $f''(x)=5>0$, তাই ফাংশনটির সর্বনিম্ন মান বিদ্যমান।\\$\therefore$ সর্বনিম্ন মান $=\frac{1}{3}\cdot2^3+\frac{1}{2}\cdot2^2-6\cdot2+8=\frac{2}{3}$।

**Final answer:** সর্বোচ্চ মান $=\frac{43}{2}$, সর্বনিম্ন মান $=\frac{2}{3}$

## ID 1387

**Question:** নিম্নলিখিত ফাংশনগুলির সর্বনিম্ন মান ও সর্বোচ্চ মান (লঘিষ্ঠ মান ও গরিষ্ঠ মান) নির্ণয় কর: (vii) $2x^3-9x^2+12x+5$

**Solution:** (vii) দেওয়া আছে, $y=2x^3-9x^2+12x+5$\\$\therefore \frac{dy}{dx}=6x^2-18x+12$\\সর্বনিম্ন বা সর্বোচ্চ মানের জন্য, $\frac{dy}{dx}=0$\\বা, $6x^2-18x+12=0$\\বা, $x^2-3x+2=0$\\বা, $(x-1)(x-2)=0$\\$\therefore x=1,2$\\আবার, $\frac{d^2y}{dx^2}=12x-18$\\$x=1$ হলে, $\frac{d^2y}{dx^2}=-6<0$, তাই সর্বোচ্চ মান বিদ্যমান এবং মান $=2-9+12+5=10$।\\$x=2$ হলে, $\frac{d^2y}{dx^2}=6>0$, তাই সর্বনিম্ন মান বিদ্যমান এবং মান $=16-36+24+5=9$।

**Final answer:** সর্বোচ্চ মান $=10$ এবং সর্বনিম্ন মান $=9$

## ID 1388

**Question:** নিম্নলিখিত ফাংশনগুলির সর্বনিম্ন মান ও সর্বোচ্চ মান (লঘিষ্ঠ মান ও গরিষ্ঠ মান) নির্ণয় কর: (viii) $x^3-5x^2+3x+2$

**Solution:** (viii) ধরি, $y=x^3-5x^2+3x+2$\\$\frac{dy}{dx}=3x^2-10x+3$\\সর্বনিম্ন ও সর্বোচ্চ মানের জন্য, $\frac{dy}{dx}=0$\\বা, $3x^2-10x+3=0$\\বা, $(x-3)(3x-1)=0$\\$\therefore x=3,\frac{1}{3}$\\আবার, $\frac{d^2y}{dx^2}=6x-10$\\$x=3$ হলে, $\frac{d^2y}{dx^2}=8>0$, তাই ফাংশনটির সর্বনিম্ন মান বিদ্যমান।\\$\therefore$ সর্বনিম্ন মান $=3^3-5\cdot3^2+3\cdot3+2=-7$।\\$x=\frac{1}{3}$ হলে, $\frac{d^2y}{dx^2}=-8<0$, তাই ফাংশনটির সর্বোচ্চ মান বিদ্যমান।\\$\therefore$ সর্বোচ্চ মান $=\left(\frac{1}{3}\right)^3-5\left(\frac{1}{3}\right)^2+3\cdot\frac{1}{3}+2=\frac{67}{27}$।

**Final answer:** সর্বনিম্ন মান $=-7$, সর্বোচ্চ মান $=\frac{67}{27}$

## ID 1389

**Question:** নিম্নলিখিত ফাংশনগুলির সর্বনিম্ন মান ও সর্বোচ্চ মান (লঘিষ্ঠ মান ও গরিষ্ঠ মান) নির্ণয় কর: (ix) $x^3-2x^2+x-10$

**Solution:** (ix) ধরি, $y=f(x)=x^3-2x^2+x-10$\\$\frac{dy}{dx}=3x^2-4x+1$\\সর্বনিম্ন ও সর্বোচ্চ মানের জন্য, $\frac{dy}{dx}=0$\\বা, $3x^2-4x+1=0$\\বা, $(x-1)(3x-1)=0$\\$\therefore x=1$ অথবা $x=\frac{1}{3}$\\এখন, $\frac{d^2y}{dx^2}=6x-4$\\$x=1$ হলে, $\frac{d^2y}{dx^2}=2>0$, তাই ফাংশনটির লঘুমান বিদ্যমান।\\লঘুমান $=1^3-2\cdot1^2+1-10=-10$।\\$x=\frac{1}{3}$ হলে, $\frac{d^2y}{dx^2}=-2<0$, তাই ফাংশনটির গরিষ্ঠমান বিদ্যমান।\\গরিষ্ঠমান $=\left(\frac{1}{3}\right)^3-2\left(\frac{1}{3}\right)^2+\frac{1}{3}-10=-\frac{266}{27}$।

**Final answer:** লঘুমান $=-10$, গরিষ্ঠমান $=-\frac{266}{27}$

## ID 1390

**Question:** নিম্নলিখিত ফাংশনগুলির সর্বনিম্ন মান ও সর্বোচ্চ মান (লঘিষ্ঠ মান ও গরিষ্ঠ মান) নির্ণয় কর: (x) $2x^3-3x^2-12x+30$

**Solution:** (x) ধরি, $f(x)=2x^3-3x^2-12x+30$\\$\therefore f'(x)=6x^2-6x-12$\\চরমমানের জন্য, $f'(x)=0$ হবে।\\বা, $6x^2-6x-12=0$\\বা, $x^2-x-2=0$\\বা, $(x-2)(x+1)=0$\\$\therefore x=-1,2$\\আবার, $f''(x)=12x-6$\\$f''(-1)=-18<0$ এবং $f''(2)=18>0$।\\$\therefore x=-1$ এর জন্য ফাংশনটির বৃহত্তম মান এবং $x=2$ এর জন্য ফাংশনটির ক্ষুদ্রতম মান বিদ্যমান।\\বৃহত্তম মান $=f(-1)=37$।\\ক্ষুদ্রতম মান $=f(2)=10$।

**Final answer:** বৃহত্তম মান $=37$, ক্ষুদ্রতম মান $=10$

## ID 1391

**Question:** নিম্নলিখিত ফাংশনগুলির সর্বনিম্ন মান ও সর্বোচ্চ মান (লঘিষ্ঠ মান ও গরিষ্ঠ মান) নির্ণয় কর: (xi) $\frac{2}{3}x^3+\frac{11}{2}x^2-6x+5$

**Solution:** (xi) ধরি, $f(x)=\frac{2}{3}x^3+\frac{11}{2}x^2-6x+5$\\$\therefore f'(x)=2x^2+11x-6$\\ফাংশনের ক্ষুদ্রতম বা বৃহত্তম মানের জন্য, $f'(x)=0$\\বা, $2x^2+11x-6=0$\\বা, $(x+6)(2x-1)=0$\\$\therefore x=-6,\frac{1}{2}$\\আবার, $f''(x)=4x+11$\\$f''(-6)=-13<0$ এবং $f''\left(\frac{1}{2}\right)=13>0$।\\সুতরাং $x=-6$ এর জন্য ফাংশনটির বৃহত্তম মান এবং $x=\frac{1}{2}$ এর জন্য ফাংশনটির ক্ষুদ্রতম মান পাওয়া যায়।\\বৃহত্তম মান $=f(-6)=95$।\\এবং ক্ষুদ্রতম মান $=f\left(\frac{1}{2}\right)=\frac{83}{24}$।

**Final answer:** বৃহত্তম মান $=95$, ক্ষুদ্রতম মান $=\frac{83}{24}$

## ID 1392

**Question:** নিম্নলিখিত ফাংশনগুলির সর্বনিম্ন মান ও সর্বোচ্চ মান (লঘিষ্ঠ মান ও গরিষ্ঠ মান) নির্ণয় কর: (xii) $2x^3-7x^2+4x+5$

**Solution:** (xii) দেওয়া আছে, $g(x)=2x^3-7x^2+4x+5$\\$\therefore g'(x)=6x^2-14x+4$ এবং $g''(x)=12x-14$\\চরমমান ও ক্ষুদ্রমানের জন্য, $g'(x)=0$\\বা, $6x^2-14x+4=0$\\বা, $(x-2)(3x-1)=0$\\$\therefore x=2,\frac{1}{3}$\\$x=2$ হলে, $g''(x)=10>0$, তাই ফাংশনটির লঘুমান বিদ্যমান।\\লঘুমান $=g(2)=16-28+8+5=1$।\\$x=\frac{1}{3}$ হলে, $g''(x)=-10<0$, তাই ফাংশনটির গরিষ্ঠমান বিদ্যমান।\\গরিষ্ঠমান $=g\left(\frac{1}{3}\right)=\frac{152}{27}$।

**Final answer:** লঘুমান $=1$, গরিষ্ঠমান $=\frac{152}{27}$

## ID 1393

**Question:** নিম্নলিখিত ফাংশনগুলির সর্বনিম্ন মান ও সর্বোচ্চ মান (লঘিষ্ঠ মান ও গরিষ্ঠ মান) নির্ণয় কর: (xiii) $x^3-6x^2+9x+1$

**Solution:** (xiii) ধরি, $f(x)=x^3-6x^2+9x+1$\\$\therefore f'(x)=3x^2-12x+9$\\লঘু ও গুরুমানের জন্য, $f'(x)=0$\\বা, $3x^2-12x+9=0$\\বা, $x^2-4x+3=0$\\বা, $(x-3)(x-1)=0$\\$\therefore x=1,3$\\আবার, $f''(x)=6x-12$\\$x=3$ হলে, $f''(x)=6>0$, তাই লঘুমান বিদ্যমান।\\লঘুমান $=3^3-6(3)^2+9\cdot3+1=1$।\\$x=1$ হলে, $f''(x)=-6<0$, তাই গুরুমান বিদ্যমান।\\গুরুমান $=1^3-6(1)^2+9\cdot1+1=5$।

**Final answer:** গুরুমান $=5$, লঘুমান $=1$

## ID 1394

**Question:** নিম্নলিখিত ফাংশনগুলির সর্বনিম্ন মান ও সর্বোচ্চ মান (লঘিষ্ঠ মান ও গরিষ্ঠ মান) নির্ণয় কর: (xiv) $54x-(2x-7)^3$

**Solution:** (xiv) ধরি, $g(x)=54x-(2x-7)^3$\\$g'(x)=54-3(2x-7)^2\cdot2=54-6(2x-7)^2$\\এবং $g''(x)=-6\cdot2(2x-7)\cdot2=-48x+168$\\লঘুমান ও গুরুমানের জন্য, $g'(x)=0$\\বা, $54-6(2x-7)^2=0$\\বা, $(2x-7)^2=9$\\$\therefore x=2,5$\\এখন, $g''(2)=72>0$, তাই $x=2$ বিন্দুতে লঘুমান আছে এবং লঘুমান $=54(2)-(2\cdot2-7)^3=135$।\\আবার, $g''(5)=-72<0$, তাই $x=5$ বিন্দুতে গরিষ্ঠ মান আছে এবং গরিষ্ঠমান $=54(5)-(2\cdot5-7)^3=243$।

**Final answer:** লঘুমান $=135$, গরিষ্ঠমান $=243$

## ID 1395

**Question:** নিম্নলিখিত ফাংশনগুলির সর্বনিম্ন মান ও সর্বোচ্চ মান (লঘিষ্ঠ মান ও গরিষ্ঠ মান) নির্ণয় কর: (xv) $\frac{\ln 2x}{x}$

**Solution:** (xv) মনে করি, $f(x)=\frac{\ln(2x)}{x}$\\$f'(x)=\frac{x\cdot\frac{2}{2x}-\ln(2x)\cdot1}{x^2}=\frac{1-\ln(2x)}{x^2}$\\এবং $f''(x)=\frac{x^2\left(-\frac{2}{2x}\right)-(1-\ln2x)2x}{x^4}=\frac{-3+2\ln2x}{x^3}$\\চরমমানের জন্য, $f'(x)=0$\\বা, $1-\ln(2x)=0$\\বা, $\ln2x=1$\\$\therefore x=\frac{e}{2}$\\এখন, $f''\left(\frac{e}{2}\right)=\frac{-8}{e^3}<0$\\$\therefore x=\frac{e}{2}$ এর জন্য $f(x)$ এর গরিষ্ঠমান আছে।\\গরিষ্ঠমান $=f\left(\frac{e}{2}\right)=\frac{\ln e}{e/2}=\frac{2}{e}$।

**Final answer:** গরিষ্ঠমান $=\frac{2}{e}$

## ID 1396

**Question:** নিম্নলিখিত ফাংশনগুলির সর্বনিম্ন মান ও সর্বোচ্চ মান (লঘিষ্ঠ মান ও গরিষ্ঠ মান) নির্ণয় কর: (xvi) $2x^3-3x^2-12x+1$

**Solution:** (xvi) ধরি, $h(x)=2x^3-3x^2-12x+1$\\$\therefore h'(x)=6x^2-6x-12$\\$\therefore h''(x)=12x-6$\\চরমবিন্দুর জন্য, $h'(x)=0$\\বা, $6x^2-6x-12=0$\\বা, $x^2-x-2=0$\\বা, $(x+1)(x-2)=0$\\$\therefore x=-1,2$\\$x=-1$ বিন্দুতে, $h''(x)=-18<0$, তাই $h(x)$ এর গরিষ্ঠমান বিদ্যমান এবং এর মান $=8$।\\$x=2$ বিন্দুতে, $h''(x)=18>0$, তাই $h(x)$ এর লঘুমান বিদ্যমান এবং এর মান $=-19$।

**Final answer:** গরিষ্ঠমান $=8$, লঘুমান $=-19$

## ID 1397

**Question:** নিম্নলিখিত ফাংশনগুলির সর্বনিম্ন মান ও সর্বোচ্চ মান (লঘিষ্ঠ মান ও গরিষ্ঠ মান) নির্ণয় কর: (xvii) $x^3-9x^2+24x-12$

**Solution:** (xvii) মনে করি, $f(x)=x^3-9x^2+24x-12$\\$\therefore f'(x)=3x^2-18x+24$ এবং $f''(x)=6x-18$\\চরমমানের জন্য, $f'(x)=0$\\বা, $3x^2-18x+24=0$\\বা, $x^2-6x+8=0$\\বা, $(x-4)(x-2)=0$\\$\therefore x=2,4$\\$x=2$ এর জন্য, $f''(x)=-6<0$, তাই $x=2$ বিন্দুতে গরিষ্ঠমান বিদ্যমান এবং এর মান $=8$।\\$x=4$ বিন্দুতে, $f''(x)=6>0$, তাই $x=4$ বিন্দুতে লঘুমান বিদ্যমান এবং এর মান $=4$।

**Final answer:** গরিষ্ঠমান $=8$, লঘুমান $=4$

## ID 1398

**Question:** $3x^4+4x^3-12x^2$, $-2<x<1$ ব্যবধিতে ফাংশনের চরম মান নির্ণয় কর।

**Solution:** (iv) ধরি, $f(x)=3x^4+4x^3-12x^2$\\$\therefore f'(x)=12x^3+12x^2-24x$\\সর্বোচ্চ ও সর্বনিম্ন মানের জন্য, $f'(x)=0$\\বা, $12x^3+12x^2-24x=0$\\বা, $x(x^2+x-2)=0$\\বা, $x(x+2)(x-1)=0$; $\therefore x=0,-2,1$\\এখানে, $0\in(-2,1)$ কিন্তু $-2,1\notin(-2,1)$।\\আবার, $f''(x)=36x^2+24x-24$\\$f''(0)=-24<0$\\$\therefore x=0$ বিন্দুতে $f(x)$ এর সর্বোচ্চ মান বিদ্যমান এবং উক্ত মান $f(0)=0$।\\$\therefore$ চরম মান $=0$।

**Final answer:** চরম মান $=0$

## ID 1399

**Question:** দেখাও যে, $x=\frac{\pi}{6}$ বিন্দুতে $\sqrt{3}\sin x+3\cos x$ ফাংশনটির সর্বোচ্চ মান বিদ্যমান এবং উক্ত মান নির্ণয় কর।

**Solution:** (v) ধরি, $y=\sqrt{3}\sin x+3\cos x$\\$\therefore \frac{dy}{dx}=\sqrt{3}\cos x-3\sin x$\\সর্বোচ্চ ও সর্বনিম্ন মানের জন্য, $\frac{dy}{dx}=0$\\বা, $\sqrt{3}\cos x-3\sin x=0$\\বা, $\tan x=\frac{1}{\sqrt{3}}$\\বা, $\tan x=\tan\frac{\pi}{6}$; $\therefore x=\frac{\pi}{6}$\\আবার, $\frac{d^2y}{dx^2}=-\sqrt{3}\sin x-3\cos x$\\যখন $x=\frac{\pi}{6}$ তখন, $\frac{d^2y}{dx^2}=-\sqrt{3}\cdot\frac{1}{2}-3\cdot\frac{\sqrt{3}}{2}=-2\sqrt{3}<0$\\অতএব, $x=\frac{\pi}{6}$ বিন্দুতে ফাংশনটির সর্বোচ্চ মান বিদ্যমান।\\$\therefore$ নির্ণেয় সর্বোচ্চ মান $=\sqrt{3}\sin\frac{\pi}{6}+3\cos\frac{\pi}{6}=2\sqrt{3}$।

**Final answer:** $x=\frac{\pi}{6}$ বিন্দুতে সর্বোচ্চ মান বিদ্যমান এবং সর্বোচ্চ মান $=2\sqrt{3}$

## ID 1400

**Question:** দেখাও যে, $x=\frac{\pi}{3}$ বিন্দুতে $\sin x(1+\cos x)$ ফাংশনটির আপেক্ষিক বৃহত্তম মান রয়েছে।

**Solution:** (vi) ধরি, $y=\sin x(1+\cos x)=\sin x+\sin x\cos x$\\$\therefore \frac{dy}{dx}=\cos x+\cos^2x-\sin^2x$\\লঘুতম ও বৃহত্তম মানের জন্য, $\frac{dy}{dx}=0$\\বা, $\cos x+\cos^2x-\sin^2x=0$\\বা, $\cos x+2\cos^2x-1=0$\\বা, $\cos x=\frac{1}{2}$; অতএব $x=\frac{\pi}{3}$।\\আবার, $\frac{d^2y}{dx^2}=-\sin x-2\sin2x$\\$x=\frac{\pi}{3}$ হলে, $\frac{d^2y}{dx^2}=-\frac{\sqrt{3}}{2}-2\cdot\frac{\sqrt{3}}{2}=-\frac{3\sqrt{3}}{2}<0$\\অতএব $x=\frac{\pi}{3}$ বিন্দুতে ফাংশনটির আপেক্ষিক বৃহত্তম মান রয়েছে।

**Final answer:** $x=\frac{\pi}{3}$ বিন্দুতে আপেক্ষিক বৃহত্তম মান রয়েছে

## ID 1401

**Question:** $0<x<\frac{\pi}{2}$ ব্যবধিতে $Y=4+2\tan x\cos x-3\tan^2x\cos^2x$ অথবা $Y=1+2\sin x+3\cos^2x$ ফাংশনটির চরম মান নির্ণয় কর।

**Solution:** (ix) প্রদত্ত রাশি $4+2\tan x\cos x-3\tan^2x\cos^2x$\\$=4+2\frac{\sin x}{\cos x}\cos x-3\frac{\sin^2x}{\cos^2x}\cos^2x$\\$=4+2\sin x-3\sin^2x$\\$=4+2\sin x+3(\cos^2x-1)$\\$=1+2\sin x+3\cos^2x$\\ধরি, $f(x)=1+2\sin x+3\cos^2x$\\$f'(x)=2\cos x-6\sin x\cos x$\\সর্বোচ্চ ও সর্বনিম্ন মানের জন্য, $f'(x)=0$\\বা, $2\cos x(1-3\sin x)=0$\\$\therefore x=\frac{\pi}{2}$ অথবা $x=\sin^{-1}\frac{1}{3}$।\\আবার, $f''(x)=-2\sin x-6\cos2x$\\$x=\frac{\pi}{2}$ বিন্দুতে $f''(x)=4>0$, তাই সর্বনিম্ন মান $=1+2(1)+3(0)^2=3$।\\$x=\sin^{-1}\frac{1}{3}$ বিন্দুতে $f''(x)=-\frac{16}{3}<0$, তাই সর্বোচ্চ মান $=1+2\cdot\frac{1}{3}+3\left(1-\frac{1}{9}\right)=\frac{13}{3}$।

**Final answer:** সর্বনিম্ন মান $=3$, সর্বোচ্চ মান $=\frac{13}{3}$

## ID 1402

**Question:** Type-IV. 6.(i) দেখাও যে, $f(x)=x^3-3x^2+18x+15$ একটি $x$ এর ক্রমবর্ধমান ফাংশন।

**Solution:** 6.(i) প্রদত্ত ফাংশন $f(x)=x^3-3x^2+18x+15$\\$\therefore f'(x)=3x^2-6x+18=3x^2-6x+3+15$\\$=3(x^2-2x+1)+15=3(x-1)^2+15$\\স্পষ্টতই $x$ এর সকল বাস্তব মানের জন্য $f'(x)>0$।\\সুতরাং প্রদত্ত ফাংশনটি $x$ এর একটি ক্রমবর্ধমান ফাংশন।

**Final answer:** প্রদত্ত ফাংশনটি $x$ এর একটি ক্রমবর্ধমান ফাংশন

## ID 1403

**Question:** Type-IV. 6.(ii) দেখাও যে, $f(x)=1-x-x^3$ একটি $x$ এর ক্রমহ্রাসমান ফাংশন।

**Solution:** (ii) দেওয়া আছে, $f(x)=1-x-x^3$\\$\therefore f'(x)=-1-3x^2=-(1+3x^2)$\\স্পষ্টতই $x$ এর সকল বাস্তব মানের জন্য $f'(x)<0$।\\সুতরাং প্রদত্ত ফাংশনটি $x$ এর একটি ক্রমহ্রাসমান ফাংশন।

**Final answer:** প্রদত্ত ফাংশনটি $x$ এর একটি ক্রমহ্রাসমান ফাংশন

## ID 1404

**Question:** Type-IV. 6.(iii) যে সকল ব্যবধিতে $f(x)=x^3-3x+5$ ফাংশনটি বৃদ্ধি বা হ্রাস পায়, সেই সকল ব্যবধি নির্ণয় কর।

**Solution:** (iii) প্রদত্ত ফাংশন $f(x)=x^3-3x+5$\\$f'(x)=3x^2-3=3(x^2-1)=3(x+1)(x-1)$\\$x=-1$ এবং $x=1$ হলে $f'(x)=0$।\\এখন $x<-1$, $-1<x<1$ এবং $x>1$ এই তিনটি ব্যবধিতে চিহ্ন পরীক্ষা করি।\\$x<-1$ ব্যবধিতে $x+1<0$ এবং $x-1<0$ হওয়ায় $f'(x)>0$, তাই ফাংশনটি বৃদ্ধি পায়।\\$-1<x<1$ ব্যবধিতে $x+1>0$ এবং $x-1<0$ হওয়ায় $f'(x)<0$, তাই ফাংশনটি হ্রাস পায়।\\$x>1$ ব্যবধিতে $x+1>0$ এবং $x-1>0$ হওয়ায় $f'(x)>0$, তাই ফাংশনটি বৃদ্ধি পায়।\\অতএব ফাংশনটি $x<-1$ ও $x>1$ ব্যবধিতে বৃদ্ধি পায় এবং $-1<x<1$ ব্যবধিতে হ্রাস পায়।

**Final answer:** $x<-1$ ও $x>1$ ব্যবধিতে বৃদ্ধি পায়; $-1<x<1$ ব্যবধিতে হ্রাস পায়

## ID 1405

**Question:** Type-IV. 6.(iv) $f(x)=2x^3-3x^2-12x+30$ ফাংশনটি কোন ব্যবধিতে বৃদ্ধি পায় এবং কোন ব্যবধিতে হ্রাস পায় তা নির্ণয় কর।

**Solution:** (iv) $f(x)=2x^3-3x^2-12x+30$\\$f'(x)=6x^2-6x-12=6(x^2-x-2)=6(x+1)(x-2)$\\$x=-1$ এবং $x=2$ হলে $f'(x)=0$ হয়।\\$x<-1$ ব্যবধিতে $x+1<0$ এবং $x-2<0$ কাজেই $f'(x)>0$; ফাংশনটি বৃদ্ধি পায়।\\$-1<x<2$ ব্যবধিতে $x+1>0$ এবং $x-2<0$ কাজেই $f'(x)<0$; ফাংশনটি হ্রাস পায়।\\$x>2$ ব্যবধিতে $x+1>0$ এবং $x-2>0$ কাজেই $f'(x)>0$; ফাংশনটি বৃদ্ধি পায়।\\$\therefore$ নির্ণেয় ফাংশনটি $x<-1$ ও $x>2$ ব্যবধিতে বৃদ্ধি পায় এবং $-1<x<2$ ব্যবধিতে হ্রাস পায়।

**Final answer:** $x<-1$ ও $x>2$ ব্যবধিতে বৃদ্ধি পায়; $-1<x<2$ ব্যবধিতে হ্রাস পায়

## ID 1406

**Question:** Type-IV. 6.(v) $f(x)=3x^2-2x+4$, $-1\le x\le2$ ফাংশনটি কোন ব্যবধিতে বৃদ্ধি পায়, কোন ব্যবধিতে হ্রাস পায় তা নির্ণয় কর।

**Solution:** (v) প্রদত্ত ফাংশন: $f(x)=3x^2-2x+4$\\$f'(x)=6x-2=2(3x-1)$\\এখন, $f'(x)=0$ বা, $2(3x-1)=0$ বা, $x=\frac{1}{3}$।\\$x=\frac{1}{3}$ বিন্দু $-1\le x\le2$ ব্যবধিকে $-1\le x<\frac{1}{3}$ ও $\frac{1}{3}<x\le2$ ব্যবধিতে বিভক্ত করে।\\$-1\le x<\frac{1}{3}$ ব্যবধিতে $3x-1<0$, তাই $f'(x)<0$।\\$\therefore -1\le x<\frac{1}{3}$ ব্যবধিতে ফাংশনটি হ্রাস পায়।\\আবার, $\frac{1}{3}<x\le2$ ব্যবধিতে $3x-1>0$, তাই $f'(x)>0$।\\$\therefore \frac{1}{3}<x\le2$ ব্যবধিতে ফাংশনটি বৃদ্ধি পায়।

**Final answer:** $-1\le x<\frac{1}{3}$ ব্যবধিতে হ্রাস পায়; $\frac{1}{3}<x\le2$ ব্যবধিতে বৃদ্ধি পায়

## ID 1407

**Question:** Type-IV. 6.(vi) যে সকল ব্যবধিতে $f(x)=x^3-6x^2+9x+5$ এ বর্ণিত ফাংশনটির মান বৃদ্ধি বা হ্রাস পায় তা নির্ণয় কর।

**Solution:** (vi) $f(x)=x^3-6x^2+9x+5$\\বা, $f'(x)=3x^2-12x+9$\\$f'(x)=0$ হলে, $3x^2-12x+9=0$\\বা, $x^2-4x+3=0$\\বা, $(x-3)(x-1)=0$; $\therefore x=1,3$\\এখন, $1$ ও $3$ বিন্দু দুই দ্বারা বাস্তব সংখ্যারেখা তিনটি ব্যবধিতে বিভক্ত হলো: $x<1$, $1<x<3$ এবং $x>3$।\\$x<1$ বা $x>3$ ব্যবধিতে $f'(x)>0$।\\এবং $1<x<3$ ব্যবধিতে $f'(x)<0$।\\$\therefore x<1$ বা $x>3$ ব্যবধিতে ফাংশনটির মান বৃদ্ধি পায় এবং $1<x<3$ ব্যবধিতে ফাংশনটির মান হ্রাস পায়।

**Final answer:** $x<1$ ও $x>3$ ব্যবধিতে বৃদ্ধি পায়; $1<x<3$ ব্যবধিতে হ্রাস পায়

## ID 1408

**Question:** Type-IV. 6.(vii) $g(x)=x^3-9x^2+15x+7$ ফাংশনটির মান যেসব ব্যবধিতে বৃদ্ধি বা হ্রাস পায় তা নির্ণয় কর।

**Solution:** (vii) দেওয়া আছে, $g(x)=x^3-9x^2+15x+7$\\আমরা জানি, $g(x)$ ফাংশনের মান বৃদ্ধি পেলে $g'(x)>0$ এবং $g(x)$ ফাংশনের মান হ্রাস পেলে $g'(x)<0$ হবে।\\$g'(x)=3x^2-18x+15$\\$g'(x)=0$ হলে, $3x^2-18x+15=0$\\বা, $x^2-6x+5=0$\\বা, $(x-5)(x-1)=0$\\$\therefore x=1,5$\\এখন, $x=1$ ও $x=5$ মানদ্বয় সকল বাস্তব সংখ্যারেখাকে $x<1$, $1<x<5$ এবং $x>5$ ব্যবধিতে বিভক্ত করে।\\$x<1$ ব্যবধিতে $g'(x)>0$, তাই $g(x)$ ফাংশনটির মান বৃদ্ধি পায়।\\$1<x<5$ ব্যবধিতে $g'(x)<0$, তাই $g(x)$ ফাংশনটির মান হ্রাস পায়।\\$x>5$ ব্যবধিতে $g'(x)>0$, তাই $g(x)$ ফাংশনটির মান বৃদ্ধি পায়।

**Final answer:** $x<1$ ও $x>5$ ব্যবধিতে বৃদ্ধি পায়; $1<x<5$ ব্যবধিতে হ্রাস পায়

## ID 1409

**Question:** Type-IV. 6.(viii) দেখাও যে, $x^3-3x^2+10x$ একটি ক্রমবর্ধমান ফাংশন।

**Solution:** (viii) ধরি, $f(x)=x^3-3x^2+10x$\\$\therefore f'(x)=3x^2-6x+10=3\left(x^2-2x+\frac{10}{3}\right)$\\$=3\left\{x^2-2x+1+\frac{10}{3}-1\right\}=3\left\{(x-1)^2+\frac{7}{3}\right\}$\\$\therefore$ সকল বাস্তব মানের জন্য $f'(x)>0$।\\$\therefore$ প্রদত্ত ফাংশনটি একটি ক্রমবর্ধমান ফাংশন।

**Final answer:** প্রদত্ত ফাংশনটি একটি ক্রমবর্ধমান ফাংশন

## ID 1410

**Question:** Type-IV. 6.(ix) $g(x)=17-15x+9x^2-x^3$ ফাংশনটি কোন ব্যবধিতে হ্রাস পায় এবং বৃদ্ধি পায় তা নির্ণয় কর।

**Solution:** (ix) দেওয়া আছে, $g(x)=17-15x+9x^2-x^3$\\আমরা জানি, $g(x)$ ফাংশনের মান বৃদ্ধি পেলে $g'(x)>0$ এবং মান হ্রাস পেলে $g'(x)<0$ হবে।\\এখন, $g'(x)=-15+18x-3x^2$\\$g'(x)=0$ হলে, $-15+18x-3x^2=0$\\বা, $3x^2-18x+15=0$\\বা, $x^2-6x+5=0$\\বা, $(x-5)(x-1)=0$\\$\therefore x=1,5$\\এখন, $x=1$ ও $x=5$ মানদ্বয় সকল বাস্তব সংখ্যারেখাকে $x<1$, $1<x<5$ এবং $x>5$ ব্যবধিতে বিভক্ত করে।\\যেহেতু, $x<1$ ব্যবধিতে $g'(x)<0$, সুতরাং $x<1$ ব্যবধিতে $g(x)$ ফাংশনটির মান হ্রাস পায়।\\আবার, $1<x<5$ ব্যবধিতে $g'(x)>0$ বলে $1<x<5$ ব্যবধিতে $g(x)$ ফাংশনটির মান বৃদ্ধি পায়।\\এবং $x>5$ ব্যবধিতে $g'(x)<0$।\\$\therefore x>5$ ব্যবধিতে $g(x)$ ফাংশনটির মান হ্রাস পায়।

**Final answer:** $x<1$ ও $x>5$ ব্যবধিতে হ্রাস পায়; $1<x<5$ ব্যবধিতে বৃদ্ধি পায়

## ID 1411

**Question:** Type-V. 7.(i) $y^2=2x$ একটি পরাবৃত্ত হলে, $(1,4)$ বিন্দু হতে পরাবৃত্তটির নিকটতম বিন্দুর স্থানাঙ্ক নির্ণয় কর।

**Solution:** 7.(i) ধরি, নির্ণেয় বিন্দু $P(x,y)$।\\$AP$ দূরত্ব $=\sqrt{(x-1)^2+(y-4)^2}$\\$\therefore AP^2=(x-1)^2+(y-4)^2$\\$\therefore AP^2=\left(\frac{y^2}{2}-1\right)^2+(y-4)^2$\\এখন, $\frac{d(AP^2)}{dy}=2\left(\frac{y^2}{2}-1\right)\frac{2y}{2}+2(y-4)$\\$=y^3-2y+2y-8=y^3-8$\\সর্বোচ্চ বা সর্বনিম্ন মানের জন্য, $\frac{d(AP^2)}{dy}=0$\\বা, $y^3-8=0$; $\therefore y=2$\\$y=2$ হলে, $x=2$।\\$\therefore$ নির্ণেয় বিন্দু $=(2,2)$।

**Final answer:** নির্ণেয় বিন্দু $(2,2)$

## ID 1412

**Question:** Type-V. 7.(ii) চিত্রে জানালার পরিসীমা 30m হলে, সর্বোচ্চ পরিমাণ আলো প্রবেশের জন্য $x$ ও $y$ নির্ণয় কর।

**Solution:** (ii) চিত্র অনুযায়ী, $AD$ চাপ $=\pi x$।\\জানালার পরিসীমা $2x+2y+\pi x$\\প্রশ্নমতে, $2x+2y+\pi x=30$\\এবং জানালার ক্ষেত্রফল, $A=2xy+\frac{\pi x^2}{2}$\\$=2x\left(\frac{30-2x-\pi x}{2}\right)+\frac{\pi x^2}{2}$\\$=30x-2x^2-\frac{\pi x^2}{2}$\\সর্বোচ্চ মানের জন্য, $\frac{dA}{dx}=0$\\বা, $30-4x-\pi x=0$\\$\therefore x=\frac{30}{\pi+4}$।\\আবার, $\frac{d^2A}{dx^2}=-4-\pi<0$\\$\therefore x=\frac{30}{\pi+4}$ এর জন্য সর্বোচ্চ মান পাওয়া যাবে।\\$\therefore 2x=\frac{60}{\pi+4}$\\$\therefore y=\frac{30-2x-\pi x}{2}=\frac{30}{\pi+4}$।\\$\therefore x$ ও $y$ এর মান যথাক্রমে $\frac{30}{\pi+4}$ ও $\frac{30}{\pi+4}$।

**Final answer:** $x=\frac{30}{\pi+4}$ এবং $y=\frac{30}{\pi+4}$

## ID 1413

**Question:** Type-V. 7.(iii) একটি সিলিন্ডারের ব্যাসার্ধ 30cm হলে সর্বনিম্ন ক্ষেত্রফলের জন্য উচ্চতা নির্ণয় কর, যখন আয়তন ধ্রুবক। সর্বনিম্ন ক্ষেত্রফলও নির্ণয় কর।

**Solution:** (iii) ধরি, সিলিন্ডারের আয়তন $V=\pi r^2h$\\এবং ক্ষেত্রফল, $A=2\pi r^2+2\pi rh$\\$\therefore A=2\pi r^2+2\pi r\cdot\frac{V}{\pi r^2}=2\pi r^2+\frac{2V}{r}$\\$\therefore \frac{dA}{dr}=4\pi r-\frac{2V}{r^2}$\\$\therefore \frac{d^2A}{dr^2}=4\pi+\frac{4V}{r^3}$\\সর্বোচ্চ বা সর্বনিম্ন ক্ষেত্রফলের জন্য, $\frac{dA}{dr}=0$\\$\therefore 4\pi r-\frac{2V}{r^2}=0$\\বা, $4\pi r^3=2V=2\pi r^2h$\\$\therefore h=2r$\\যেহেতু, $r=30$ cm, উচ্চতা $h=2r=60$ cm।\\সর্বনিম্ন ক্ষেত্রফল $A_{\min}=2\pi r^2+2\pi rh=2\pi(30)^2+2\pi\cdot30\cdot60=5400\pi$ বর্গ সেমি।

**Final answer:** উচ্চতা $60$ cm এবং সর্বনিম্ন ক্ষেত্রফল $5400\pi$ বর্গ সেমি

## ID 1414

**Question:** Type-V. 7.(iv) নির্দিষ্ট আয়তনের কোণ আকৃতির তাঁবুর আকার কেমন হলে কাপড়ের জন্য সর্বনিম্ন খরচ হবে?

**Solution:** (iv) ধরি, কোণের উচ্চতা $h$, হেলানো উচ্চতা $l$ ও ব্যাসার্ধ $r$।\\$V=\frac{1}{3}\pi r^2h$\\এবং কোণের ক্ষেত্রফল, $A=\pi rl=\pi r\sqrt{h^2+r^2}$\\$\therefore A^2=\pi^2r^2(h^2+r^2)$\\$=\pi^2r^2\left(\frac{9V^2}{\pi^2r^4}+r^2\right)$\\$\therefore A^2=\frac{9V^2}{r^2}+\pi^2r^4$\\$\therefore \frac{dA^2}{dr}=-\frac{18V^2}{r^3}+4\pi^2r^3$\\সর্বোচ্চ বা সর্বনিম্ন মানের জন্য, $-\frac{18V^2}{r^3}+4\pi^2r^3=0$\\$\Rightarrow 2\pi^2r^6=9V^2$\\$\therefore h^2=2r^2$\\$\therefore h=\sqrt{2r}$।\\এই শর্ত পূরণ হলে কাপড়ের জন্য সর্বনিম্ন খরচ হবে।

**Final answer:** $h=\sqrt{2r}$ হলে কাপড়ের জন্য সর্বনিম্ন খরচ হবে

## ID 1415

**Question:** Type-V. 7.(v) দুইটি সংখ্যার যোগফল 12; এদের একটি সংখ্যার ঘন এর সাথে অপর সংখ্যার গুণফল গঠিত হলে সংখ্যাগুলি নির্ণয় কর।

**Solution:** (v) ধরি, একটি সংখ্যা $x$।\\$\therefore$ অন্য সংখ্যাটি $(12-x)$\\এখন, তাদের ফাংশন $f(x)=x^3(12-x)$\\$\therefore f(x)=12x^3-x^4$\\$f'(x)=36x^2-4x^3=4x^2(9-x)$\\$f''(x)=72x-12x^2$\\গঠিত গুণফলের সর্বোচ্চ মানের জন্য, $f'(x)=0$\\বা, $4x^2(9-x)=0$\\$\therefore x=9$\\$x=9$ হলে, $f''(x)=72\cdot9-12\cdot9^2=-324<0$\\$\therefore x=9$ এর জন্য গুণফল সর্বোচ্চ হবে।\\সুতরাং একটি সংখ্যা $9$ এবং অপর সংখ্যাটি $(12-9)$ বা $3$।

**Final answer:** সংখ্যা দুটি $9$ এবং $3$

## ID 1416

**Question:** Type-VI. 8.(i) $f(x)=x^2$ এর লেখচিত্র ব্যবহার করে $(2.1)^2$ এর আনুমানিক নির্ণয় কর।

**Solution:** 8.(i) মনে করি, $x_0=2$ এবং $x_0+\delta x=2.1$।\\$\therefore \delta x=0.1$\\এবং $f(x)=x^2$ বা, $f'(x)=2x$\\$f'(2)=2\times2=4$\\$f(x_0+\delta x)\approx f(x_0)+f'(x_0)\delta x$\\বা, $f(2.1)\approx f(2)+f'(2)\times0.1$\\$\therefore (2.1)^2\approx2^2+4\times0.1=4.4$।

**Final answer:** আনুমানিক মান $(2.1)^2\approx4.4$

## ID 1417

**Question:** Type-VI. 8.(ii) $x=0$ বিন্দুর সন্নিকটে $f(x)=\sqrt{1+x}$ বক্ররেখার ঐ বিন্দুতে স্পর্শকের রেখা দ্বারা সমীকৃত করে $\sqrt{0.9}$ এবং $\sqrt{1.1}$ এর আসন্ন মান নির্ণয় কর।

**Solution:** (ii) $f(x)=\sqrt{1+x}\Rightarrow f'(x)=\frac{1}{2\sqrt{1+x}}$\\$\therefore f(0)=1$ এবং $f'(0)=\frac{1}{2}$\\$x=0$ বিন্দুর সন্নিকটে $f(x)=\sqrt{1+x}$ এর ফাংশনের লেখচিত্রকে ঐ বিন্দুতে অঙ্কিত স্পর্শক রেখা দ্বারা স্থানীয়ভাবে প্রতিস্থাপন করে পাই,\\$f(x)\approx f(0)+f'(0)(x-0)$\\বা, $\sqrt{1+x}\approx1+\frac{1}{2}x$\\(i) $x=-0.1$ বসিয়ে পাই, $\sqrt{1-0.1}\approx1+\frac{1}{2}(-0.1)=0.95$\\অর্থাৎ, $\sqrt{0.9}\approx0.95$।\\(ii) $x=0.1$ বসিয়ে পাই, $\sqrt{1+0.1}\approx1+\frac{1}{2}(0.1)=1.05$\\অর্থাৎ, $\sqrt{1.1}\approx1.05$।

**Final answer:** $\sqrt{0.9}\approx0.95$ এবং $\sqrt{1.1}\approx1.05$

## ID 1418

**Question:** Type-VI. 9.(i) $x=1$ বিন্দুতে $y=x^2$ ফাংশনের অন্তরক আকার সমীকরণ থেকে $dy$ এবং $\delta y$ নির্ণয় কর যখন $dx=\delta x=2$।

**Solution:** 9.(i) ধরি, $f(x)=y=x^2$।\\$\therefore \frac{dy}{dx}=2x$ বা, $dy=2x\,dx$\\বা, $dy=2\times1\times2$; $[x=1, dx=2]$\\$\therefore dy=4$।\\আবার, $\delta y=f(x+\delta x)-f(x)$\\$=f(1+2)-f(1)=f(3)-f(1)$\\$=3^2-1^2=9-1=8$।

**Final answer:** $dy=4$ এবং $\delta y=8$

## ID 1419

**Question:** Type-VI. 9.(ii) $x=3$ বিন্দুতে $y=\frac{x^2}{3}+1$ ফাংশনের অন্তরক আকার সমীকরণ থেকে $dy$ এবং $\delta y$ নির্ণয় কর যখন $dx=\delta x=3$।

**Solution:** (ii) ধরি, $f(x)=y=\frac{x^2}{3}+1$\\$\therefore \frac{dy}{dx}=\frac{2}{3}x$ বা, $dy=\frac{2}{3}x\,dx$\\বা, $dy=\frac{2}{3}\times3\times3$; $[x=3, dx=3]$\\$\therefore dy=6$।\\আবার, $\delta y=f(x+\delta x)-f(x)$\\$=f(3+3)-f(3)=f(6)-f(3)$\\$=\left(\frac{6^2}{3}+1\right)-\left(\frac{3^2}{3}+1\right)=12-3=9$।

**Final answer:** $dy=6$ এবং $\delta y=9$

## ID 1420

**Question:** Type-VI. 9.(iii) $y=\frac{1}{2}x^2$ এর ক্ষেত্রে অঙ্কন কর এবং তাতে $\delta y$ ও $dy$ চিহ্নিত কর। $x=3$ ও $\delta x=dx=3$ হলে $\delta y$ ও $dy$ নির্ণয় কর।

**Solution:** (iii) নিম্নে $y=\frac{1}{2}x^2$ ক্ষেত্রে অঙ্কন করে তাতে $\delta y$ ও $dy$ চিহ্নিত করা হলো।\\$x=3$ ও $\delta x=dx=3$ হলে,\\$\delta y=f(x+\delta x)-f(x)=f(3+3)-f(3)$\\$=f(6)-f(3)=\frac{1}{2}(6^2-3^2)=\frac{1}{2}(36-9)=13.5$।\\এখন $f(x)=y=\frac{1}{2}x^2$, তাই $f'(x)=x$।\\$\therefore dy=f'(x)\,dx=f'(3)\times3=3\times3=9$।

**Final answer:** $\delta y=13.5$ এবং $dy=9$

## ID 1421

**Question:** বিগত বছরের ইঞ্জিনিয়ারিং ও বিশ্ববিদ্যালয় ভর্তি পরীক্ষায় লিখিত প্রশ্ন। 10. $f(x)=x^5-5x^4+5x^3-1$ ফাংশনের সর্বোচ্চ ও সর্বনিম্ন মান নির্ণয় কর।

**Solution:** 10. দেওয়া আছে, $f(x)=x^5-5x^4+5x^3-1$\\$f'(x)=5x^4-20x^3+15x^2$\\এবং $f''(x)=20x^3-60x^2+30x$\\সর্বোচ্চ ও সর্বনিম্ন মানের জন্য, $f'(x)=0$\\বা, $5x^4-20x^3+15x^2=0$\\বা, $5x^2(x^2-4x+3)=0$\\বা, $x^2(x-1)(x-3)=0$\\$\therefore x=0,3,1$।\\এখন, $f''(0)=0$।\\$f''(1)=20-60+30=-10<0$, অর্থাৎ $x=1$ এর জন্য সর্বোচ্চ মান বিদ্যমান।\\$\therefore$ সর্বোচ্চ মান $f(1)=1-5+5-1=0$।\\আবার, $f''(3)=20\cdot3^3-60\cdot3^2+30\cdot3=90>0$, অর্থাৎ $x=3$ এর জন্য সর্বনিম্ন মান বিদ্যমান।\\$\therefore$ সর্বনিম্ন মান $f(3)=3^5-5\cdot3^4+5\cdot3^3-1=-28$।

**Final answer:** সর্বোচ্চ মান $=0$ এবং সর্বনিম্ন মান $=-28$

## ID 1422

**Question:** বিগত বছরের ইঞ্জিনিয়ারিং ও বিশ্ববিদ্যালয় ভর্তি পরীক্ষায় লিখিত প্রশ্ন। 11. $F(x)=x+2\sin x$ হলে $[0,2\pi]$ ব্যবধিতে লঘুমান ও গুরুমান নির্ণয় কর। $(0,2\pi)$ ব্যবধিতে $F(x)$ এর আনতি বিন্দু (Point of inflection) সৃষ্টি থাকলে নির্ণয় কর।

**Solution:** 11. দেওয়া আছে, $F(x)=x+2\sin x$\\লঘুমান ও গুরুমানের জন্য, $F'(x)=1+2\cos x=0$\\বা, $\cos x=-\frac{1}{2}=\cos\frac{2\pi}{3}$\\$\therefore x=2n\pi\pm\frac{2\pi}{3}$; $[n\in\mathbb{Z}]$\\$n=0$ হলে, $x=\pm\frac{2\pi}{3}$ এবং $n=1$ হলে, $x=\frac{8\pi}{3},\frac{4\pi}{3}$।\\$[0,2\pi]$ ব্যবধিতে $x$ এর গ্রহণযোগ্য মান $\frac{2\pi}{3},\frac{4\pi}{3}$।\\এখানে, $F''(x)=-2\sin x$\\$F''\left(\frac{2\pi}{3}\right)=-2\sin\frac{2\pi}{3}=-\sqrt{3}<0$\\$F''\left(\frac{4\pi}{3}\right)=-2\sin\frac{4\pi}{3}=\sqrt{3}>0$\\$\therefore$ লঘুমান $=F\left(\frac{4\pi}{3}\right)=\frac{4\pi}{3}+2\sin\frac{4\pi}{3}=\frac{4\pi}{3}-\sqrt{3}$।\\এবং গুরুমান $=F\left(\frac{2\pi}{3}\right)=\frac{2\pi}{3}+2\sin\frac{2\pi}{3}=\frac{2\pi}{3}+\sqrt{3}$।\\আবার, $F''(x)=0$ হলে, $-2\sin x=0$, তাই $x=\pi$।\\$x=\pi$ এর পূর্বে ও পরে $F''(x)$ বিপরীত চিহ্নবিশিষ্ট।\\$\therefore x=\pi$ এর জন্য আনতি বিন্দু বিদ্যমান।\\আনতি বিন্দু $=(\pi,\pi)$।

**Final answer:** লঘুমান $=\frac{4\pi}{3}-\sqrt{3}$, গুরুমান $=\frac{2\pi}{3}+\sqrt{3}$ এবং আনতি বিন্দু $(\pi,\pi)$
