import { useCallback } from "react";
import styles from "./../css/navbar.module.css";
import logo from "./../../public/assets/iconWhiteText.png"


const Navbar = () => {
  const onFrameLogoffceClick = useCallback(() => {
    // Please sync "/Login" to the project
  }, []);

  return (
    <header className="Navbar">
      <img src="./../../public/assets/iconWhiteText.png" alt="logo" className="logo"/>


      <div className={styles.fRAMELogo}>
        <div className={styles.frameHubAbout}>
          <div className={styles.logo}>
            <img className={styles.image1Icon} alt="" src={logo} />
          </div>
          <div className={styles.logo1}>
            <img className={styles.image1Icon1} alt="" src={logo} />
          </div>
        </div>
        <div className={styles.textButton}>
          <div className={styles.navLinks}>
            <div className={styles.hub}>Hub</div>
            <div className={styles.rectangleVegetables}>
              <div className={styles.products}>Products</div>
              <img
                className={styles.akarIconschevronDown}
                alt=""
                src="/akariconschevrondown.svg"
              />
            </div>
            <div className={styles.about}>About</div>
          </div>
        </div>
      </div>
      <div className={styles.rectangleFood}>
        <div className={styles.headerText}>
          <div className={styles.searchBox}>
            <img
              className={styles.testimonialStarsIcon}
              alt=""
              src="/testimonial-stars.svg"
            />
            <input
              className={styles.searchForAnything}
              placeholder="Search for anything"
              type="text"
            />
          </div>
          <div className={styles.searchBox1}>
            <img className={styles.icon} alt="" src="/testimonial-stars.svg" />
            <div className={styles.searchForAnythingContainer}>
              <span className={styles.search}>{`Search `}</span>
              <span className={styles.forAnything}>for anything</span>
            </div>
          </div>
        </div>
        <button className={styles.frameLogoffce} onClick={onFrameLogoffceClick}>
          <div className={styles.logIn}>Log In</div>
        </button>
      </div>
    </header>
  );
};

export default Navbar;
